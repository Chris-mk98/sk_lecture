import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False


class Sales_data:
    def __init__(self):
        self.dates= pd.date_range('2024-01-01', '2024-12-31', freq='D')

        self.sales = {
            'Date' : self.dates,
            'Sales' : np.random.randint(1000,10000,len(self.dates))
        }
        
        self.df = pd.DataFrame(self.sales)
        self.df['Month'] = self.df['Date'].dt.month


    
    def visualize(self): 
        self.pivot = pd.pivot_table(self.df, values='Sales', index='Month', aggfunc='sum').reset_index()

        plt.plot([i for i in range(1,13)], self.pivot['Sales'], marker = 'o')

        plt.title("월별 매출 총합")
        plt.xlabel("월")
        plt.ylabel("매출")

        plt.show()

if __name__ == '__main__':
    sales_data = Sales_data()
    sales_data.visualize()