import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# x = [i for i in range(6)]
# y = [2*i for i in range(6)]

# plt.plot(x, y, marker='o', linestyle='-', color='b', label='test')

# plt.title("Test")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.legend()

# ctgy = ['a', 'b', 'c', 'd', 'e']
# val = [5,7,3,8,4]

# plt.barh(ctgy, val, align='center', color='skyblue', edgecolor='red')
# plt.ylim(0,8)

# plt.show()

# data = np.random.randn(1000)
# print(data)

# plt.hist(data,bins=20,color='orange', edgecolor='black', alpha=0.7)

# plt.show()

# data = np.random.rand(10,10)
# mask = np.triu(np.ones_like(data, dtype=bool))

# sns.heatmap(data, annot=True, mask=mask, cmap='coolwarm')
# plt.title('Heatmap Example')
# plt.show()

# tips = sns.load_dataset('tips')

# sns.boxplot(x='day', y='total_bill', data=tips, palette='Set2')
# plt.title('Boxbplot')
# plt.show()

# sns.violinplot(x="day", y="total_bill", data=tips,
# palette="muted", split=True)
# plt.title("Violin Plot Example: Total Bill by Day")
# plt.show()


# 고객 정보 데이터프레임
customers = pd.DataFrame({
'customer_id': [1, 2, 3],
'name': ['Alice', 'Bob', 'Charlie']
})
# 주문 정보 데이터프레임
orders = pd.DataFrame({
'order_id': [101, 102, 103],
'customer_id': [1, 2, 4],
'product': ['Laptop', 'Tablet', 'Smartphone']
})

result_1 = pd.merge(customers, orders, on='customer_id', how='inner')

result_2 = pd.merge(customers, orders, on='customer_id', how='')

print(result_1)
print(result_2)
