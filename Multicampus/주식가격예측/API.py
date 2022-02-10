import pymysql
import pandas as pd

class function_API:
    def __init__(self):
        #MySQL 연결
        self.conn = pymysql.connect(host='host', user='user', 
                password='password', db='DB_name', charset='utf8')

    def get_info(self, company, start, end):
        try:
            # with self.conn.cursor() as cur:
            #     sql = f"""
            #     SELECT a.company, b.* 
            #     FROM company_info a, daily_price b
            #     WHERE b.date BETWEEN '{start}' AND '{end}'
            #     AND a.code = b.code
            #     AND a.company = '{company}'
            #     """
            #     cur.execute(sql)
            
            #회사명, 조회 시작일, 조회 종료일 기준으로 검색
            sql = f"""
                SELECT a.company, b.* 
                FROM company_info a, daily_price b
                WHERE b.date BETWEEN '{start}' AND '{end}'
                AND a.code = b.code
                AND a.company = '{company}'
                """

            # rows = cur.fetchall()

            #데이터 프레임에 저장
            df = pd.read_sql(sql, self.conn)

            # self.display_info(rows)
            self.display_info(df)

        except Exception as e:
            print('Exception occured :', str(e))

    def display_info(self, df):
        #데이터프레임의 모든 열을 생략 없이 출력하도록 설정
        pd.set_option('display.max_rows', None)

        # df = pd.DataFrame(rows, columns=['회사명', '종목코드', '날짜', \
        #         '시가', '종가', '고가', '저가', '전일비', '거래량'])
        
        #날짜를 인덱스로 지정
        df.index = df['date']

        #데이터프레임 출력
        print(df)
