def DFS(curr):
    #방문쳌
    visited[curr] = True
    print(chr(curr+65), end=' ')

    #방문하지 않고 인접한 정점으로 이동
    for i in adj_list[curr]:
        if not visited[i]:
            DFS(i)


V, E = map(int, input().split())

adj_list = [[] for _ in range(V)] #인접리스트
visited = [False] * V #방문쳌을 위한

for i in range(E):
    st, ed = map(int, input().split())
    adj_list[st].append(ed)  # 여기서 끝내면 방향성있는 표시
    adj_list[ed].append(st)

DFS(3)