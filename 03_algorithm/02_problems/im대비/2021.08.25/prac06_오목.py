import sys

sys.stdin = open("test_06.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    result = 'NO'

    while True:
        for i in range(len(arr)): #가로
            if result == 'YES':
                break
            cnt = 0
            # flag = False
            for j in range(len(arr[0])):
                if arr[i][j] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        # flag = True
                        result = 'YES'
                        break

                elif arr[i][j] == '.':
                    # flag = False
                    cnt = 0

        for j in range(len(arr[0])): #세로
            if result == 'YES':
                break
            cnt = 0
            # flag = False
            for i in range(len(arr)):
                if arr[i][j] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        # flag = True
                        result = 'YES'
                        break

                elif arr[i][j] == '.':
                    # flag = False
                    cnt = 0

        for i in range(len(arr)):  # 오른쪽으로 대각선
            if result == 'YES':
                break
            for j in range(len(arr[0])):
                if result == 'YES':
                    break
                cnt = 0
                for k in range(0, 5):
                    if 0 <= i + k < len(arr) and 0 <= j + k < len(arr[0]):
                        if arr[i + k][j + k] == 'o':
                            cnt += 1
                            if cnt >= 5:
                                result = 'YES'
                                break

        for i in range(len(arr)):  # 왼쪽 대각선
            if result == 'YES':
                break
            for j in range(len(arr[0])):
                if result == 'YES':
                    break
                cnt = 0
                for k in range(0, 5):
                    if 0 <= i + k < len(arr) and 0 <= j - k < len(arr[0]):
                        if arr[i + k][j - k] == 'o':
                            cnt += 1
                            if cnt >= 5:
                                result = 'YES'
                                break

        break




    print('#{} {}'.format(tc, result))