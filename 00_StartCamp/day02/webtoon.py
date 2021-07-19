"""
2021.07.15
SSAFY StartCamp day02
양명균쌤 네이버 웹툰 순위 크롤링
"""

import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/index'

response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')

# 각 개체말고 살짝 위 클릭, li에 a 태그 안에 텍스트 있음
ranking = data.select('#realTimeRankFavorite > li > a')

# for 문 이용 뽑아오기 (enumerate 추후 설명 예정)
for rank, name in enumerate(ranking):
    print(rank+1, name.text)