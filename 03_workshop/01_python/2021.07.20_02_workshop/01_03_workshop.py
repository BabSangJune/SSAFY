"""
날짜 : 2021.07.20
학습 : SSAFY 01_03_workshop
제목 : 계단 만들기
문제 :
자연수 number를 입력 받아, 아래와 같이 높이가 number인 내려가는 계단을 출력하시오.

입력 : 4
출력 :
1
1 2
1 2 3
1 2 3 4
"""

num = int(input())

for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end='')

    print()