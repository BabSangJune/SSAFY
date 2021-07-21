"""
날짜 : 2021.07.21
학습 : SSAFY 01_03_workshop
제목 : 3.
문제 :
정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는
all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

입력 :
출력 :
"""

def all_list_sum(lis):
    tot = 0
    for i in range(len(lis)):
        for j in range(i+1):
            tot += lis[i][j]

    return tot



print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])) # 55