"""
날짜 : 2021.07.19
학습 : SSAFY 01_02_workshop
제목 : 거꾸로 세로로 출력하기
문제 :
자연수 number를 입력 받아, number부터 0까지의 수를 세로로 한줄씩 출력하시오.

입력 : 5
출력 : 
5
4
3
2
1
0
"""

num = int(input())

for i in range(num, -1, -1):
    print(i)