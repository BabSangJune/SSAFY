MAP = [
    [3, 2, 1, 2],
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 8, 7, 6]
]

r, c = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for t in range(4):
    nr = r + dr[t]
    nc = c + dc[t]
    if nr < 0 or nc < 0 or nr >= 4 or nc >= 4: continue
    if t == 0: print("위:", end='')
    if t == 1: print("아래:", end='')
    if t == 2: print("왼:", end='')
    if t == 3: print("오른:", end='')

    print(MAP[nr][nc])

# print(MAP[r-1][c+0]) # 상
# print(MAP[r+1][c+0]) # 하
# print(MAP[r+0][c-1]) # 좌
# print(MAP[r+0][c+1]) # 우


de = -1