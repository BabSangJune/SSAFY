from bs4.element import ResultSet
import requests

from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
USD = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
result = USD.text
#print(result)

print(f'USD 환율은 {result}입니다.')