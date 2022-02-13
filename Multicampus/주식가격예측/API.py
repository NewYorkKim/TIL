import pymysql
import pandas as pd
from datetime import datetime, timedelta
import re

class function_API:
    def __init__(self):
        #MySQL 연결
        self.conn = pymysql.connect(host='host', user='user', 
                password='password', db='DB_name', charset='utf8')
        
        #빈 딕셔너리 생성 >> 종목코드, 회사명 저장
        self.codes = {}

        #get_company_info 호출
        self.get_company_info()

    def __del__(self):
        #MySQL 연결 해제
        self.conn.close()

    def get_company_info(self): #DB에서 회사 정보 가져오기
        sql = "SELECT * FROM company_info"
        df = pd.read_sql(sql, self.conn)
        for idx in range(len(df)): #딕셔너리에 종목코드, 회사명 저장
            self.codes[df['code'].values[idx]] = df['company'].values[idx]


    def get_daily_price(self, code, start_date=None, end_date=None):
        """KRX 종목의 주식 정보를 데이터프레임 형태로 반환
           -code : 종목코드 또는 회사명
           -start_date : 조회 시작일, 미입력 시 1년 전 오늘 날짜
           -end_date : 조회 종료일, 미입력 시 오늘 날짜
        """
        if start_date is None: #조회 시작일을 미입력한 경우
            one_year_ago = datetime.today() - timedelta(days=365)
            start_date = one_year_ago.strftime('%Y-%m-%d')
            print(f"start_date is initialized to {start_date}")

        else: #조회 시작일을 입력한 경우
            start_lst = re.split('\D+', start_date) #분리

            start_year = int(start_lst[0])
            start_month = int(start_lst[1])
            start_day = int(start_lst[2])

            #잘못된 값을 받은 경우
            if start_year < 1900 or start_year > 2200:
                print(f"ValueError : start_year({start_year}) is wrong.")
                return 
            if start_month < 1 or start_month > 12:
                print(f"ValueError : start_month({start_month}) is wrong.")
                return
            if start_day > 1 or start_day > 31:
                print(f"ValueError : start_day({start_day}) is wrong.")
                return

            start_date = f"{start_year:04d}-{start_month:02d}-{start_date:02d}"

        if end_date is None: #조회 종료일을 미입력한 경우
            end_date = datetime.today().strftime('%Y-%m-%d')
            print(f"end_daye is initialized to {end_date}")

        else: #조회 종료일을 입력한 경우
            end_lst = re.split('\D+', end_date) #분리

            end_year = int(end_lst[0])
            end_month = int(end_lst[1])
            end_day = int(end_lst[2])

            #잘못된 값을 받은 경우
            if end_year < 1900 or end_year > 2200:
                print(f"ValueError : end_year({end_year}) is wrong.")
                return
            if end_month < 1 or end_month > 12:
                print(f"ValueError : end_month({end_month}) is wrong.")
                return
            if end_day < 1 or end_day > 31:
                print(f"ValueError : end_day({end_day}) is wrong.")
                return

            end_date = f"{end_year:04d}-{end_month:02d}-{end_day:02d}"

        #종목코드와 회사명을 각각 리스트로 저장
        codes_keys = list(self.codes.keys)
        codes_values = list(self.codes.values())

        if code in codes_keys: #종목코드를 받은 경우
            pass
        elif code in codes_values: #회사명을 받은 경우 >> 종목코드로 재설정
            idx = codes_values.index(code)
            code = codes_keys[idx]
        else: #잘못된 값을 받은 경우
            print(f"ValueError : Code({code}) doesn't exist.")

        #DB에서 조건에 해당하는 data를 검색
        sql = f"SELECT * FROM daily_price WHERE code = '{code}\
            AND date >= '{start_date}' AND date <='{end_date}'"

        #결과를 데이터프레임 형태로 저장
        df = pd.read_sql(sql, self.conn)
        #날짜 칼럼을 인덱스로 지정
        df.index = df['date']

        return df