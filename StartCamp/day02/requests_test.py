import requests
from bs4 import BeautifulSoup

# response = requests.get("https://www.naver.com")
response = requests.get("https://www.naver.com").text
# response = requests.get("https://www.naver.com").status_code


print(response)