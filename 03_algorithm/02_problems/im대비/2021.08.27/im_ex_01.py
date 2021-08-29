"""
SS텔레콤에서 현재 기지국의 위치와 집들이 표시된 지도를 2차원 n x n 배열로 변환
"""
import sys

sys.stdin = open('ex_01.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = [list(input()) for _ in range(N)]

    cnt = 0
    home = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'H':
                home += 1

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'A':
                for k in range(1, 2):
                    if 0 <= i - k < N and 0 <= j < N and arr[i - k][j] == 'H':  # 상
                        cnt += 1
                        arr[i - k][j] = 'X'
                    if 0 <= i + k < N and 0 <= j < N and arr[i + k][j] == 'H':  # 하
                        cnt += 1
                        arr[i + k][j] = 'X'
                    if 0 <= i < N and 0 <= j - k < N and arr[i][j - k] == 'H':  # 좌
                        cnt += 1
                        arr[i][j - k] = 'X'
                    if 0 <= i < N and 0 <= j + k < N and arr[i][j + k] == 'H':  # 우
                        cnt += 1
                        arr[i][j + k] = 'X'

            elif arr[i][j] == 'B':
                for k in range(1, 3):
                    if 0 <= i - k < N and 0 <= j < N and arr[i - k][j] == 'H':  # 상
                        cnt += 1
                        arr[i - k][j] = 'X'
                    if 0 <= i + k < N and 0 <= j < N and arr[i + k][j] == 'H':  # 하
                        cnt += 1
                        arr[i + k][j] = 'X'
                    if 0 <= i < N and 0 <= j - k < N and arr[i][j - k] == 'H':  # 좌
                        cnt += 1
                        arr[i][j - k] = 'X'
                    if 0 <= i < N and 0 <= j + k < N and arr[i][j + k] == 'H':  # 우
                        cnt += 1
                        arr[i][j + k] = 'X'

            elif arr[i][j] == 'C':
                for k in range(1, 4):
                    if 0 <= i - k < N and 0 <= j < N and arr[i - k][j] == 'H':  # 상
                        cnt += 1
                        arr[i - k][j] = 'X'
                    if 0 <= i + k < N and 0 <= j < N and arr[i + k][j] == 'H':  # 하
                        cnt += 1
                        arr[i + k][j] = 'X'
                    if 0 <= i < N and 0 <= j - k < N and arr[i][j - k] == 'H':  # 좌
                        cnt += 1
                        arr[i][j - k] = 'X'
                    if 0 <= i < N and 0 <= j + k < N and arr[i][j + k] == 'H':  # 우
                        cnt += 1
                        arr[i][j + k] = 'X'

    print(home - cnt)

'''
1
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
'''
