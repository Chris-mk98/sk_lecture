import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

class CustomerSalesAnalysis:
    def __init__(self, data):
        # 데이터 생성
        self.data = data
        self.df = pd.DataFrame(self.data)

        # 월 컬럼 추가 / 결제액 컬럼 추가
        self.df['구매일자'] = pd.to_datetime(self.df['구매일자'])
        self.df['월'] = self.df['구매일자'].dt.month
        self.df['결제액'] = self.df['수량'] * self.df['단가']
    
    def monthly_sales(self):
        # 월별 결제액 그룹화
        groupby = self.df.groupby('월')['결제액'].sum().reset_index()

        plt.bar(groupby['월'], groupby['결제액'], color = 'skyblue' )
        plt.title('월별 매출 총합')
        plt.xlabel('월')
        plt.ylabel('매출')
        plt.show()
    
    def cumulative_sales(self):
        # 고객별 결제액 그룹화
        groupby = self.df.groupby('고객명')['결제액'].sum().reset_index()
        
        plt.pie(groupby['결제액'], labels=groupby['고객명'], autopct='%.1f%%')
        plt.title('고객별 누적 매출 비율')
        plt.show()



if __name__ == '__main__':
    # 데이터 초기화
    data = {
    '고객명': ['홍길동', '이영희', '김철수', '박지수', '최민호', '홍길동', '이영희', '김철수'],
    '구매일자': ['2024-01-10', '2024-02-14', '2024-02-18', '2024-03-05', '2024-03-20', '2024-04-10', '2024-04-25', '2024-05-05'],
    '상품명': ['노트북', '키보드', '모니터', '노트북', '마우스', '모니터', '노트북', '키보드'],
    '수량': [1, 2, 1, 2, 4, 2, 1, 3],
    '단가': [1500000, 50000, 300000, 1500000, 20000, 300000, 1500000, 50000]
}
    result = CustomerSalesAnalysis(data)
    result.cumulative_sales()
    result.monthly_sales()


