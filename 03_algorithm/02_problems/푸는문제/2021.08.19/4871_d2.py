"""
날짜 : 2021.08.19
학습 : SWEA D2
제목 : 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
문제 :
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤100
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다
E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.
3 #t
6 5 #start, end
1 4 #간선 정보 시작1
1 3
2 3
2 5
4 6 #end 5니까 5개
1 6 #출발 도착
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
#1 1
#2 1
#3 1
"""


def dfs(st, ed):
    stack = []
    stack.append(st)

    while stack:
        curr = stack.pop()

        if curr == ed:
            return 1

        if not visited[curr]:
            visited[curr] = True

            for i in range(len(Node[curr])):
                if Node[curr][i] and not visited[Node[curr][i]]:
                    stack.append(Node[curr][i])
    return 0

T = int(input()) #tc 갯수
for tc in range(1, T+1):
    V, E = map(int, input().split()) #V,E
    Node = [[] for _ in range(V+1)]
    visited = [False] * (V+1)

    for _ in range(E):
        st, ed = map(int, input().split())
        Node[st].append(ed)

    start, end = map(int, input().split())

    result = dfs(start, end)

    print('#{} {}'.format(tc, result))


