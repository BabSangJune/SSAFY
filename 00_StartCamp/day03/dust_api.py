"""
2021.07.16
SSAFY StartCamp day03
미세먼지 농도 출력
"""

import requests

key = ''
local = '부산'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={local}&returnType=json'


#실습 
#부산의 미세먼지 농도는 OOOOO입니다. 

result = requests.get(url).json()

dust = result['response']['body']['items'][2]['pm10Value']
print(f'부산태종대의 미세먼지 농도는 {dust}입니다.')


#아래처럼 차례대로 접근도 가능하다.. 
# response_dict = result['response']
# body = response_dict['body']
# items = body['items']