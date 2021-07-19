"""
2021.07.15
SSAFY StartCamp day02
이름으로 국가 예측
"""
# oo의 국적은 00%로 00입니다.

import requests

name = 'june'
url = f'https://api.nationalize.io?name={name}'

response = requests.get(url).json()

# print(response, type(response))

name = response['name']
country_id = response['country'][0]['country_id']
country_probability = response['country'][0]['probability']*100

print(f'{name}의 국적은 {country_probability}%로 {country_id}입니다.')