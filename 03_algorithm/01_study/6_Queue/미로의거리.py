def BFS():
    Q = [[S, 0]]
    visited = [S]

    while Q:
        v, dist = Q.pop(0)
        if v == G:
            return dist

        for i in range(1, V + 1):
            if adj_arr[v][i] == 1 and i not in visited:
                Q.append([i, dist + 1])
                visited.append(i)
    return 0


def BFS2():
    Q = [S]
    visited = [False] * (V + 1)
    visited[S] = True
    dist = 0

    while Q:
        size = len(Q)
        # Q size로 묶어서 현재 같은 레벨의 친구들만 돈다.
        for _ in range(size):
            v = Q.pop(0)

            if v == G: return dist

            for i in range(1, V + 1):
                if visited[i] == False and adj_arr[v][i] == 1:
                    Q.append(i)
                    visited[i] = True

        dist += 1
    return 0

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_arr = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        A, B = map(int, input().split())
        adj_arr[A][B] = adj_arr[B][A] = 1

    S, G = map(int, input().split())

    print("#{} {}".format(tc, BFS()))
