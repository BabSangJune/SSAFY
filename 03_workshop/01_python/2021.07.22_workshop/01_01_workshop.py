"""
날짜 : 2021.07.22
학습 : SSAFY 01_01_workshop
제목 : 1. 숫자의 의미
문제 :
정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인
문자열을 반환하는 get_secret_word 함수를 작성하시오.
단, list는 65이상 90이하그리고 97이상 122이하의 정수로만 구성되어 있다.

입력 :
출력 :
"""

def get_secret_word(nums):
    cnt = ''
    for i in range(len(nums)):
        cnt += chr(nums[i])

    return f'\'{cnt}\''


print(get_secret_word([83, 115, 65, 102, 89])) #'SsAfY'