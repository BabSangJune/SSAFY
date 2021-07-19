"""
2021.07.16
SSAFY StartCamp day03
텔레그램 챗봇
"""


import requests

TOKEN = ''
APP_URL = f'https://api.telegram.org/bot{TOKEN}'

#응답 내용 저장하기
update_url = f'{APP_URL}/getUpdates'
response = requests.get(update_url).json()

#chat_id 뽑아내기

chat_id = response.get('result')[0].get('message').get('chat').get('id')
### 메시지를 보내보자..
#필수 조건
# 1. chat_id
# 2. text

text = '승훈님 별다방 아메리카노 당첨!'

message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)

# 미세먼지 잠깐 연습
city = 1132599
url = f'https://www.metaweather.com/api/location/{city}/'

response = requests.get(url).json()

tommorow_weather = response.get('consolidated_weather')[2].get('weather_state_name')

message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={tommorow_weather}'

requests.get(message_url)