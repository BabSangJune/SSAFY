arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# r = 1 #2846
r = 0  # 8513 주의 파이썬은 음수 인덱스 사용함
c = 1
N = 3
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 위나 아래나 똑같음
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# di, dj | dx, dy | dy, dx

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    # nr = r + drc[i][0]
    # nc = c + drc[i][1]
    if 0 <= nr < N and 0 <= nc < N: #범위 제한
        print(arr[nr][nc], end=' ')

    # 범위 안에 들어오지 않으면 다음 차례로
    if nr < 0 or nr >= N or nc < 0 or nc >= N:
        continue
    print(arr[nr][nc], end=' ')