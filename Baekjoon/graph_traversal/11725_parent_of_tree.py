# https://www.acmicpc.net/problem/11725
import sys
from collections import deque
input = sys.stdin.readline      # 요거 안쓰면 시간초과

# dfs Recursion Error
# bfs solved


def dfs(v):
    for w in range(len(G[v])):
        if not visited[G[v][w]]:
            visited[G[v][w]] = visited[v] + 1
            dfs(G[v][w])


def bfs(v):
    dq = deque()
    dq.append(v)

    while dq:
        v = dq.popleft()
        for edge in G[v]:
            if not visited[edge]:
                visited[edge] = visited[v] + 1
                dq.append(edge)


N = int(input())

visited = [0] * (N+1)

G = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)

visited[1] = 1
bfs(1)


for node in range(2, N+1):
    p_visited = visited[node] - 1   # 부모의 visited는 하나 작음
    for connected_node in G[node]:  # 그 노드와 이어진 노드 중
        if visited[connected_node] == p_visited:    # p_visited의 값을 가진 노드를
            print(connected_node)   # 출력
