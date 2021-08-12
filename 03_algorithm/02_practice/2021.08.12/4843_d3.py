"""
날짜 : 2021.08.12
학습 : SWEA D3
제목 : 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬
문제 :
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수,
2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다

10 1 9 2 8 3 7 4 6 5

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26


[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.
#1 10 1 9 2 8 3 7 4 6 5
#2 89 8 85 11 67 16 60 28 49 39
#3 98 3 97 9 88 17 75 18 71 21
"""

def My_max_num(num1, num2):
    if num1 < num2:
        return num2
    else:
        return num1

def MY_min_num(num1, num2):
    if num1 > num2:
        return num2
    else:
        return num1


T = int(input())
for tc in range(1, T+1):
    N = int(input()) #숫자수
    nums = list(map(int, input().split())) #숫자 리스트
    lst_result = [0] * N #빈리스트
    min_num = 987654321
    max_num = 0

    for i in range(N): #nums 돌려서 가장 큰 수 찾기
        max_num = My_max_num(nums[i], max_num)

    for j in range(1, N+1): #lst_result에 쓸 인덱스
        if j % 2 == 0 and lst_result[j] == 0: #j가 짝수이면서 인덱스 값이 0이면
            lst_result[j] += max_num #lst_result 해당 자리에 max_num 넣고

    nums.remove(max_num) #nums에서 max_num 삭제


    for i in range(N): #똑같이
        min_num = MY_min_num(nums[i], min_num)

    for j in range(1, N + 1):
        if j % 2 == 1 and lst_result[j] == 0:
            lst_result[j] += min_num

    nums.remove(min_num)

    print(lst_result[0:10])





