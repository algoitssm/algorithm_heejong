# https://www.acmicpc.net/problem/11725
from collections import deque


def dfs(v):
    visited[v] = 1

    for w in range(N+1):
        if not visited[G[v][w]]:
            dfs[G[v][w]]


N = int(input())

visited = [0] * (N+1)

G = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)  # 양방향

# print(G)

# DFS

parent_list = [0 for _ in range(N+1)]

dfs(1)

print(visited)


# BFS

# v = 1
# dq = deque()
# dq.append(v)
# visited[v] = 1
# level_list = [0 for _ in range(N+1)]

# level = 1
# num_per_level = 0

# idx = 0
# while dq:

#     v = dq.popleft()

#     for w in range(len(G[v])):
#         if not visited[G[v][w]]:
#             visited[G[v][w]] = 1
#             dq.append(G[v][w])

#             level_list[G[v][w]] = level
#             num_per_level += 1

#     else:
#         print(num_per_level)

#     if idx == num_per_level:
#         level += 1
#         idx = -1
#         num_per_level = 0

#     idx += 1


# print(G)
# print(level_list)
# print(visited)
