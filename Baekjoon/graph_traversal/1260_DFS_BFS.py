# https://www.acmicpc.net/problem/1260
from collections import deque


def dfs(v):
    visited_dfs[v] = 1
    stack_dfs.append(v)

    for w in range(len(edges[v])):
        if not visited_dfs[edges[v][w]]:
            dfs(edges[v][w])


def bfs(v):
    visited_bfs[v] = 1
    dq.append(v)

    while dq:
        v = dq.popleft()
        stack_bfs.append(v)

        for w in range(len(edges[v])):          # v에 연결점이 없으면 그냥 통과
            if not visited_bfs[edges[v][w]]:    #
                visited_bfs[edges[v][w]] = 1
                dq.append(edges[v][w])


N, M, V = map(int, input().split())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())  # 2개씩 잘라서 입력
    edges[s].append(e)                      # edges 리스트에 추가
    edges[e].append(s)      # 양방향

for edge in edges:      # 이게 없으면 들어가는 순서대로 순회
    edge.sort()

visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)
stack_dfs = []
stack_bfs = []

dq = deque()
dfs(V)
bfs(V)

print(*stack_dfs)
print(*stack_bfs)
