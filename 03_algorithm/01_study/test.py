for _ in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 0상 1하 2좌 3우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    posi_pass = 0

    for i in range(100):  # 뒤에서 부터 접근
        if ladder[-1][i] == 2:
            start = i  # 시작 열 idx

    r = 99
    c = start

    while r != 0:  # 행이 0 이 아니면 실행 (위로 올라가니까 0되면 멈춘다)

        if 0 < (c - 1) <= 99 and ladder[r][c - 1] == 1:

            while 0 < (c - 1) <= 99 and ladder[r][c - 1] > 0:
                ladder[r][c] = posi_pass
                c = c + dc[2]


        # 오른쪽
        if 0 < (c + 1) <= 99 and ladder[r][c + 1] == 1:

            while 0 < (c + 1) <= 99 and ladder[r][c + 1] > 0:
                ladder[r][c] = posi_pass
                c = c + dc[3]



        # 위로 이동
        # if ladder[r - 1][c] == 1 and 0 < r <= 100:  # 현 위치에서 위에 확인
        #     while ladder[r - 1][c] > 0 :  # 0보다 크면
        #         ladder[r][c] = posi_pass  # 현위치 0으로 바꾸고
        #         r = r + dr[0]  # 위로 이동
        #         break
        r = r + dr[0]

    print('#{} {}'.format(tc, c))