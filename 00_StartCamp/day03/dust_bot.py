"""
2021.07.16
SSAFY StartCamp day03
텔레그램 미세먼지 챗봇
"""

import requests

key = ''
local = '부산'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={local}&returnType=json'

result = requests.get(url).json()

dust = result['response']['body']['items'][2]['pm10Value']
#미세먼지 가지고오기

TOKEN = ''
APP_URL = f'https://api.telegram.org/bot{TOKEN}'

#응답 내용 저장하기
update_url = f'{APP_URL}/getUpdates'
response = requests.get(update_url).json()

#chat_id 뽑아내기

chat_id = response.get('result')[0].get('message').get('chat').get('id')
last_message = response.get('result')[-1].get('message').get('text')

text = '안녕하세요.'

if last_message == '미세먼지':
    text = f'부산태종대의 미세먼지 농도는 {dust}입니다.'


message_url = f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)