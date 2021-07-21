"""
날짜 : 2021.07.21
학습 : SSAFY 01_01_workshop
제목 : 1. List의 합 구하기
문제 :
정수로만 이루어진 list 를 전달 받아 해당 list 의 모든 요소들의 합을 반환하는 list_sum
함수를 built in 함수인 sum() 함수를 사용하지 않고 작성하시오

입력 :
출력 :
"""

nums = [1, 2, 3, 4, 5]

def list_sum(nums):
    tot = 0
    for num in nums:
        tot += num
    return tot

print(list_sum(nums))
