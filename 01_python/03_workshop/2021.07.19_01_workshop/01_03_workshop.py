"""
날짜 : 2021.07.19
학습 : SSAFY 01_03_workshop
제목 : N줄 덧셈 (SWEA #2025)
문제 :
입력으로 자연수 number가 주어질 때, 1부터 주어진 자연수 number까지를 모두 더한 값
을 출력하시오. 단, 주어지는 숫자는 10000을 넘지 않는다. 예를 들어, 주어진 숫자가 10일
경우 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55이므로, 출력해야 할 값은 55이다.

입력 : 10
출력 : 55
"""

# num = 0
# total = 0
# n = int(input())

# while num <= n:
#     total += num
#     num += 1

# print(total)

n = int(input())
tot = 0

for i in range(1, n+1):
    tot += i
print(tot)