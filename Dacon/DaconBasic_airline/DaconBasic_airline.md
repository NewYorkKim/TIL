# 데이콘 Basic: 항공사 고객 만족도 예측 대회

[항공사 고객 만족도 예측 경진대회](https://dacon.io/competitions/official/235871/overview/description)

`public: 0.939` `private: 0.928`



## 목적

항공사의 만족도 조사 정보들을 담은 데이터를 통해 각 응답자의 만족 여부 예측



## 데이터

##### train.csv : 학습데이터

- id : 샘플 아이디

- Gender : 성별
- Customer Type : Disloyal 또는 Loyal 고객
- Age : 나이
- Type of Travel : Business 또는 Personal Travel
- Class : 등급
- Flight Distance : 비행 거리
- Seat comfort : 좌석 만족도
- Departure/Arrival time convenient : 출발/도착 시간 편의성 만족도
- Food and drink : 식음료 만족도
- Gate location : 게이트 위치 만족도
- Inflight wifi service : 기내 와이파이 서비스 만족도
- Inflight entertainment : 기내 엔터테인먼트 만족도
- Online support : 온라인 지원 만족도
- Ease of Online booking : 온라인 예매 편리성 만족도
- On-board service : 탑승 서비스 만족도
- Leg room service : Leg room 서비스 만족도
- Baggage handling : 수하물 처리 만족도
- Checkin service : 체크인 서비스 만족도
- Cleanliness : 청결도 만족도
- Online boarding : 온라인보딩 만족도
- Departure Delay in Minutes : 출발 지연 시간
- Arrival Delay in Minutes : 도착 지연 시간
- target : 만족 여부

##### test.csv : 테스트 데이터

- id : 샘플 아이디
- Gender : 성별
- Customer Type : Disloyal 또는 Loyal 고객
- Age : 나이
- Type of Travel : Business 또는 Personal Travel
- Class : 등급
- Flight Distance : 비행 거리
- Seat comfort : 좌석 만족도
- Departure/Arrival time convenient : 출발/도착 시간 편의성 만족도
- Food and drink : 식음료 만족도
- Gate location : 게이트 위치 만족도
- Inflight wifi service : 기내 와이파이 서비스 만족도
- Inflight entertainment : 기내 엔터테인먼트 만족도
- Online support : 온라인 지원 만족도
- Ease of Online booking : 온라인 예매 편리성 만족도
- On-board service : 탑승 서비스 만족도
- Leg room service : Leg room 서비스 만족도
- Baggage handling : 수하물 처리 만족도
- Checkin service : 체크인 서비스 만족도
- Cleanliness : 청결도 만족도
- Online boarding : 온라인보딩 만족도
- Departure Delay in Minutes : 출발 지연 시간
- Arrival Delay in Minutes : 도착 지연 시간



## EDA

[참고](https://dacon.io/competitions/official/235871/codeshare/4420?page=1&dtype=recent)



## 모델

##### pycaret

- 상위 모델들을 결합하여 새로운 앙상블 모델 생성 
- XGBoost, catboost, LGBMClassifier



## 정리

> 다음에는 어떻게 할까?

##### Departure Delay in Minutes와 Arrival Delay in Minutes

- Departure 삭제, Arrival 기준 지연 여부 ➡ 새로운 feature 생성

  ```python
  data['Delayed'] = (data['Departure Delay in Minutes'] 
                    + data['Arrival Delay in Minutes']).apply(lambda x : 0 if x > 0 else 1)
  test['Delayed'] = (test['Departure Delay in Minutes'] 
                     + test['Arrival Delay in Minutes']).apply(lambda x : 0 if x > 0 else 1)
  ```

##### Flight Distance와 Age

- 구간 별 순차값 부여 ➡ 정규화

  ``` python
  from sklearn.preprocessing import MinMaxScaler
  
  pre_features = ['Age', 'Flight Distance']
  
  sclaer = MinMaxScaler()
  data[pre_features] = scaler.fit_transform(data[pre_features])
  ```

  