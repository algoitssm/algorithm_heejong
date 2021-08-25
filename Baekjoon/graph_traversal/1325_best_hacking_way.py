# https://www.acmicpc.net/problem/1325

# dfs RecursionError
# bfs MemoryError
# PyPy solved

import sys
from collections import deque
input = sys.stdin.readline


# def dfs(v):
#     global cnt
#     cnt += 1
#     visited[v] = 1

#     # if cnt_list[v]:
#     #     return cnt + cnt_list[v]

#     for edge in G[v]:
#         if edge and not visited[edge]:
#             dfs(edge)

#     return cnt


def bfs(v):
    global cnt
    dq = deque()
    dq.append(v)
    visited[v] = 1

    while dq:
        w = dq.popleft()
        for edge in G[w]:
            if not visited[edge]:
                visited[edge] = 1
                dq.append(edge)
                cnt += 1

    return cnt


N, M = map(int, input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    G[e].append(s)

max_cnt = 0
cnt_list = [0 for _ in range(N+1)]

for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    cnt = 1
    cnt = bfs(i)
    if max_cnt < cnt:
        max_cnt = cnt
    cnt_list[i] = cnt

for idx, val in enumerate(cnt_list):
    if val == max_cnt:
        print(idx, end=' ')
print()
