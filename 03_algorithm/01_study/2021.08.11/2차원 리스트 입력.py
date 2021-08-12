#첫 줄, 행 열 크기
# N 개의 줄에 걸쳐 입력

'''
3 4
1 2 3 4
5 6 7 8
9 1 2 3
'''

N, M = map(int, input().split())

# 1. 빈리스트를 만들어 넣고 1차 리스트 append

arr = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

# 2. 행의 공간을 미리 확보하고 해당 자리를 바꾼다
arr = [0] * N

for i in range(N):
    arr[i] = list(map(int, input().split()))

# 3. 리스트 내포

arr = [list(map(int, input().split())) for _ in range(N)]


for i in arr:
    print(*i)

###########
# N * M 크기의 0으로 가득찬 이차원 배열
arr = [[0] * M for _ in range(N)]