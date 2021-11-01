# 1. sleep
from time import sleep
def sleep_3_seconds():
    sleep(3)
    print('잘잣다')

print('이제 자야지')
sleep_3_seconds()
print('학교가야지')

# 2. requests

import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1/')
todo = response.json()

print(todo)
