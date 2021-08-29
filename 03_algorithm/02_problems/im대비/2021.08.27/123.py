import sys
sys.stdin = open('1974.txt', 'r')

T = int(input()) #tc 갯수
for tc in range(1, T+1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    good = 45 #1~9까지 합 45 검증자료

    cnt = 0
    for i in range(9):
        tot = 0
        for j in range(9):
            tot += sdoku[i][j]

        if tot == good:
            cnt += 1

    for j in range(9):
        tot = 0
        for i in range(9):
            tot += sdoku[i][j]

        if tot == good:
            cnt += 1

    for i in range(0, 9 , 3):
        tot = 0
        for j in range(0, 9, 3):
            tot = sdoku[i][j]+ sdoku[i][j+1]+sdoku[i][j+2]+sdoku[i+1][j]+sdoku[i+1][j+1]+sdoku[i+1][j+2]+sdoku[i+2][j]+sdoku[i+2][j+1]+sdoku[i+2][j+2]

        if tot == good:
            cnt += 1

    if cnt == 21:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))