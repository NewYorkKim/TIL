import pymysql
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import json, calendar
from threading import Timer

class DBupdater:
    def __init__(self):
        #MySQL 연결
        self.conn = pymysql.connect(host='host', user='user', password='password', db='DB_name', charset='utf8')

        #company_info 테이블 생성 (회사명, 종목코드, 최근 업데이트 날짜)
        with self.conn.cursor() as cur:
            sql = """
            CREATE TABLE IF NOT EXISTS company_info (
            company VARCHAR(40), 
            code VARCHAR(20) PRIMARY KEY,
            last_update DATE
            ) 
            """
            cur.execute(sql)

        #daily_price 테이블 생성 (종목코드, 날짜, 시가, 종가, 전일가, 고가, 저가, 거래량)
        with self.conn.cursor() as cur:    
            sql = """
            CREATE TABLE IF NOT EXISTS daily_price (
            code CHAR(20),
            date DATE,
            open BIGINT,
            close BIGINT,
            high BIGINT,
            low BIGINT,
            diff BIGINT,
            volume BIGINT,
            PRIMARY KEY (code, date))
            """
            cur.execute(sql)

        #변경 내용 저장
        self.conn.commit()

        #update_company_info 함수 호출
        self.update_company_info()

    def __del__(self):
        #MySQL 연결 종료
        self.conn.close()

    def read_krx_code(self): #krx에서 상장법인목록 가져오기
        url = "http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13"
        res = requests.get(url) #VSCode >> 한글 깨짐
        krx = pd.read_html(res.text)[0]
        #krx = pd.read_html(url, header=0)[0] #스파이더 >> 한글 안 깨짐

        #회사명과 종목코드에 대한 데이터만 추출, 칼럼 이름 변경
        krx = krx[['회사명', '종목코드']]
        krx = krx.rename(columns={'회사명':'company', '종목코드':'code'})
        #종목코드 6자리 유지
        krx.code = krx.code.map('{:06d}'.format)

        return krx

    def update_company_info(self): #MySQL에 회사 정보 업데이트
        with self.conn.cursor() as cur:
            #company_info 테이블에서 최근 업데이트 날짜 검색
            sql = "SELECT MAX(last_update) FROM company_info"
            cur.execute(sql)
            #최근 업데이트 날짜를 sql_date에 저장
            sql_date = cur.fetchone()
            #오늘 날짜를 today에 저장
            today = datetime.today().strftime('%Y-%m-%d')

            #만약 업데이트 기록이 없거나 최근 업데이트 날짜가 오늘이 아닐 경우
            if sql_date[0] == None or sql_date[0].strftime('%Y-%m-%d') < today:
                #read_krx_code 함수 호출 >> 최신 상장법인목록 조회 후 company_info 업데이트
                krx = self.read_krx_code()
                
                for idx in range(len(krx)):
                    code = krx.code.values[idx] #code에 종목코드 저장
                    company = krx.company.values[idx] #company에 회사명 저장
                    
                    #회사명, 종목코드 REPLACE
                    sql = f"REPLACE INTO company_info VALUES ('{company}', '{code}', '{today}')"
                    cur.execute(sql)

                self.conn.commit()

    def read_price(self, code, pages_to_fetch): #네이버 금융에서 주식 정보 가져오기
        try:
             #빈 데이터프레임 total 생성
            total = pd.DataFrame()

            #네이버 금융에서 해당 기업 주식 정보 가져오기
            url = f"http://finance.naver.com/item/sise_day.nhn?code={code}"
            headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}
            res = requests.get(url, headers=headers)
            soup = BeautifulSoup(res.text, 'lxml')

            pgrr = soup.find("td", class_="pgRR")
            if pgrr is None: #총 페이지 수가 1인 경우 pgRR 부재
                last_page = 1
            else:
                last_page = str(pgrr.a["href"]).split('=')[-1]
            
            pages = min(last_page, pages_to_fetch)

            #페이지 별 주식 정보를 total에 병합
            for page in range(1, pages + 1):
                res = requests.get(f"{url}&page={page}", headers=headers)
                # soup = BeautifulSoup(res.text, 'lxml')
                # soup_table = soup.select('table')

                table = pd.read_html(res.text)[0] 
                # table = pd.read_html(str(soup_table))[0].dropna()
                total = pd.concat([total, table])
        
            #칼럼 이름 변경
            total = total.rename(columns={'날짜':'Date', '종가':'Close', '전일비':'Diff', '시가':'Open', '고가':'High', '저가':'Low', '거래량':'Volume'})
            #날짜로 변환
            total.Date = pd.to_datetime(total.Date)
            #결측값 제거
            total = total.dropna()
            #정수 타입으로 변환
            total[['Close', 'Diff', 'Open', 'High', 'Low', 'Volume']] = total[['Close', 'Diff', 'Open', 'High', 'Low', 'Volume']].astype(int)
            #칼럼 순서 조작
            total = total[['Date', 'Open', 'Close', 'High', 'Low', 'Diff', 'Volume']]
            
        except Exception as e:
            print('Exception occured :', str(e))
            return None

        return total

    def update_daily_price(self, pages_to_fetch):
        #company_info 테이블에서 회사명과 종목코드 검색
        cur = self.conn.cursor()
        cur.execute("SELECT company, code FROM company_info")
        #codes에 모두 저장
        codes = cur.fetchall()

        #네이버 금융에서 해당기업 주식 정보 조회 후 replace_daily_price 함수 호출
        for idx, code in enumerate(codes):
            df = self.read_price(code[1], pages_to_fetch)
            
            if df is None:
                continue

            self.replace_daily_price(df, idx, code[1], code[0])

    def replace_daily_price(self, df, idx, code, company):
        #종목코드와 주식 정보를 REPLACE
        with self.conn.cursor() as cur:
            for row in df.itertuples():
                sql = f"REPLACE INTO daily_price VALUES ('{code}', \
                    '{row.Date}', {row.Open}, {row.Close}, {row.High}, {row.Low}, {row.Diff}, {row.Volume})"
                cur.execute(sql)
        self.conn.commit()

    def execute_daily(self): #매일 오후 17시에 daily_prcie 테이블 업데이트
        #update_company_info 함수 호출 
        self.update_company_info()
        
        #pages_to_fetch(페이지 수) 설정
        try:
            with open('config.json', 'r') as in_file:
                config = json.load(in_file)
                pages_to_fetch = config['pages_to_fetch']
        except FileNotFoundError: #json 파일이 없는 경우 생성
            with open('config.json', 'w') as out_file:
                pages_to_fetch = 100 
                config = {'pages_to_fetch': pages_to_fetch}
                json.dump(config, out_file)
        #update_daily_price 함수 호출
        self.update_daily_price(pages_to_fetch)
        
        #현재 날짜와 시간을 tmnow에 저장
        tmnow = datetime.now() 
        #calendar.monthrange() : 특정 연도와 특정 월의 마지막 요일과 마지막 일자를 튜플 형태로 반환
        #이번 달 마지막 일자를 lastday에 저장
        lastday = calendar.monthrange(tmnow.year, tmnow.month)[1]
        
        #tmnext 설정
        if tmnow.month == 12 and tmnow.day == lastday: 
            tmnext = tmnow.replace(year=tmnow.year+1, month=1, day=1, hour=17, minute=0, second=0)
        elif tmnow.day == lastday: 
            tmnext = tmnow.replace(montho=tmnow.month+1, day=1, hour=17, minute=0, second=0)
        else:
            tmnext = tmnow.replace(month=tmnow.day+1, hour=17, minute=0, second=0)
        
        #tmnext와 tmnow의 시간차를 tmdiff에 저장
        tmdiff = tmnext - tmnow
        #tmdiff를 초단위로 변환
        secs = tmdiff.seconds
        #secs만큼 타이머 설정 >> 매일 17시마다 daily_update 함수 실행
        t = Timer(secs, self.daily_update)
        #다음 업데이트 시간 공지
        print(f"\nWaiting for next update ({tmnext.strftime('%Y-%m-%d %H:%M')})\n")
        #타이머 시작
        t.start()

if __name__ == '__main__':
    dbu = DBupdater()
    # dbu.daily_update()


