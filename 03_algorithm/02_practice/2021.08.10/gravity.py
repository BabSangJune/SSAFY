"""
날짜 : 2021.08.10
학습 : 2021.08.10 수업
제목 : 교재 gravity
문제 :
상자들이 쌓여있는 방이 있다. 방이 오른쪽으로 90도 회전하여 상자들이
중력의 영향을 받아 낙하한다고 할 때, 낙차가 가장 큰 상자를 구하여
그 낙차를 리턴 하는 프로그램을 작성하시오.
중력은 회전이 완료된 후 적용된다.
상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며
벽에서 떨어져서 쌓인 상자는 없다.
방의 가로길이는 항상 100이며, 세로 길이도 항상 100이다.
즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다.

입력
3
9
7 4 2 0 0 6 0 7 0
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53

출력
#1 7
#2 6
#3 13
"""

'''
리스트로 만들어서 y축 길이가 가장 긴 상자를 x축 끝 인덱스 숫자와 빼면 떨어진값
여기서 상자 y축이 가장 긴 것이 여러개면 x축 가장 앞 상자 - x축 끝 인덱스 + 본인 제외 동일 높이 상자
...
이렇게 풀면 안된다. 가장 많이 떨어진 값이 아님
'''

def max_box(nums): #가장 높은 상자 구할 함수
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


# T = int(input())
#
# for tc in range(1, T+1): #테스트 케이스
#     area_width = int(input()) #가로 길이
#     box = list(map(int, input().split())) #상자 높이
#     max_height = max_box(box) #가장 긴 상자
#     cnt = 0 #값이 여러개 일때
#     drop = 0 #떨어진값
#
#     for i in range(area_width):
#         if box[i] == max_height:
#             cnt += 1
#             drop = area_width - box.index(max_height) - cnt
#
#
#     print(drop)


# 이런식으로 한칸씩 옆으로 땡겨서 변수 하나에 누적으로 더 해주고 그 값이 제일 큰것이 답
# 이거 찬솔
# T = int(input())
#
# for tc in range(1, T+1):
#     area_width = int(input())
#     box = list(map(int, input().split()))
#     max_gravity = 0
#
#     for i in range(area_width-1):
#         gravity = 0
#
#         for j in range(i+1, area_width):
#             if box[i] > box[j]:
#                 gravity += 1
#
#         if gravity > max_gravity:
#             max_gravity = gravity
#
#     print('#{} {}'.format(tc, max_gravity))

#쌤
T = int(input())

for tc in range(1, T+1):

    N = int(input())
    box = list(map(int, input().split()))

    ans = 0
    
    #전체 박스
    for i in range(N):
        cnt = 0
        
        #나 다음부터 나 보다 작은 값을 찾아 카운트
        for j in range(i+1, N):
            if box[i] > box[j]:
                cnt += 1

