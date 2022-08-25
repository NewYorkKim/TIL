from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import sqlite3

class FestivalDataUpdate:
    def __init__(self):
        self.conn = sqlite3.connect("festivals.db")

        self.get_data()
    
    def get_data(self):
        url = 'http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api'
        key = 'KYnzJga7PnoRyXNVENDQkD5Ud7cbI/o/a7h/EbKR2AjRnGNYysJgMasRSJ+nis+96bWZ1YOigVVGXUzxzKQn0w==' # decoding
        params ={'serviceKey' : key, 'pageNo' : '1', 'numOfRows' : '10000', 'type' : 'json'}
        response = requests.get(url, params=params)

        data = response.json()

        self.convert_to_df(data)

    def convert_to_df(self, data):
        df = pd.DataFrame(data['response']['body']['items'])

        self.update_db(df)

    def update_db(self, df):
        df.to_sql('festival_data', self.conn, if_exists='replace')
        self.conn.commit()

        new = pd.read_sql("SELECT * FROM festival_data", self.conn, index_col=None)
        print(new)

        self.conn.close()

        print('작업이 완료되었습니다.')

fd = FestivalDataUpdate()