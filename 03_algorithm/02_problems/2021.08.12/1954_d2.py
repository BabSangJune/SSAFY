"""
날짜 : 2021.08.12
학습 : SWEA D2
제목 : 1954 .달팽이 숫자
문제 :
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.


[예제]
N이 3일 경우,
N이 4일 경우,

[제약사항]
달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고,
그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.
2
3
4
[출력]
각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
#1
1 2 3
8 9 4
7 6 5
#2
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
"""

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)] #리스트 만들기

    # 0상, 1하, 2좌, 3우
    # dr = [-1, 1, 0, 0]
    # dc = [0, 0, -1, 1]
    #우 좌 하 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    M = 0 #우로 이동

    # 처음 시작점 [0][0] 값 1
    r = 0
    c = 0
    arr[r][c] = 1

    # 숫자 차례대로 2부터 넣기, 정사각형이니까 n**2
    for i in range(2, N ** 2 + 1):
        r += dr[M]
        c += dc[M]
        arr[r][c] = i #숫자 넣기

        #범위설정
        if 0 <= r + dr[M] < N and 0 <= c + dc[M] < N and not arr[r+dr[M]][c+dc[M]]:
            continue

        if M != 3:
            M += 1
        else:
            M = 0



    print('#{}'.format(tc))
    for i in arr:
        print(*i)