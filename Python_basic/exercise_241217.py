# import requests


# url = 'https://jsonplaceholder.typicode.com/posts'
# params = {'userID': 1}
# response = requests.get(url, params=params)

# if response.status_code == 200:
#     print('데이터 가져오기 성공')
#     print(response.text[:500])
#     data_obj = response.json()
#     for post in data_obj:
#         print('title', post['title'][:10])
#         print('body', post['body'][:10])

# else:
#     print(f'오류 발생: {response.status_code}')

# from bs4 import BeautifulSoup

# html_doc = """
#     <div class="news-item">
#         <h2 class="title">Breaking News: AI Takes Over</h2>
#         <a href="https://news.com/article123">Read More</a>
#     </div>
#     <div class="news-item">
#         <h2 class="title">Another News: Python is Awesome</h2>
#         <a href="https://news.com/article456">Read More</a>
#     </div>
# """
# # BeautifulSoup 객체 생성
# soup = BeautifulSoup(html_doc, 'html.parser')

# # CSS 선택자로 모든 .news-item 선택
# news_items = soup.select('.news-item')
# print(soup.h2)
# for item in news_items:
#     title = item.select_one('.title').text # .title 클래스의 텍스트
#     link = item.select_one('a')['href'] # 첫 번째 <a> 태그의 href 속성
#     print(f"Title: {title}")
#     print(f"Link: {link}")


import csv
import pandas as pd

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles']
]

with open('data.csv', mode='w', encoding='utf8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    print("save ok!")

data = pd.read_csv('data.csv')
print(data)

df = pd.DataFrame(data)
df.to_excel('data.xlsx', index=False, sheet_name='data1')
print('save as excel ok!')