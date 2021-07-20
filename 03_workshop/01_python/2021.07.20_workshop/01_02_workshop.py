"""
날짜 : 2021.07.20
학습 : SSAFY 01_02_workshop
제목 : 중간값 찾기 (SWEA #2063 변형)
문제 :
중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를
뜻한다. 리스트 numbers에 입력된 숫자에서 중간값을 출력하라.

입력 :
출력 : 64
"""

numbers = [
85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]

numbers.sort()

def finding(numbers):
    n = len(numbers)
    if n % 2 == 1:
        result = numbers[int((n - 1) / 2)]

    else:
        result = (numbers[int(n / 2) - 1] + numbers[int(n / 2)]) / 2

    return result



print(finding(numbers))