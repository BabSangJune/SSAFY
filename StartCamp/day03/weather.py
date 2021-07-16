"""
2021.07.16
SSAFY StartCamp day03
이틀 뒤 서울 날씨 출력
"""

import requests
from bs4 import BeautifulSoup

city = 1132599
url = f'https://www.metaweather.com/api/location/{city}/'

response = requests.get(url).json()

tommorow_weather = response.get('consolidated_weather')[2].get('weather_state_name')

print(f'서울 모레의 날씨는 {tommorow_weather} 예상합니다.')