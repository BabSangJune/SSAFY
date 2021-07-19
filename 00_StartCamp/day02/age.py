"""
2021.07.15
SSAFY StartCamp day02
양명균쌤 이름으로 나이 예측
"""

import requests

name = 'Bob'
url = f'https://api.agify.io?name={name}'

response = requests.get(url).json()

print(response, type(response))