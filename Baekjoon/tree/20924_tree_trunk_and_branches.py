# https://www.acmicpc.net/problem/20924
import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def up_to_giga(v):
    global trunk_length, giga

    visited[v] = 1

    # 루트일 때 기가인 경우
    if v == R and len(G[v]) != 1:
        giga = v
        return

    # 루트가 아닐 때 기가인 경우
    if len(G[v]) > 2:
        giga = v
        return

    for child in G[v]:
        w = child[0]
        if not visited[w]:
            trunk_length += child[1]
            up_to_giga(w)


def branch_search(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        v = q.popleft()
        for childs in G[v]:
            w = childs[0]
            d = childs[1]
            if not visited[w]:
                visited[w] = visited[v] + d
                q.append(w)


N, R = map(int, input().split())

G = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, d = map(int, input().split())
    G[a].append((b, d))
    G[b].append((a, d))


# print(G)
visited = [0 for _ in range(N+1)]

trunk_length = 0
giga = 0
up_to_giga(R)
# print(visited)
# print(trunk_length)
# print(giga)

# visited = [0 for _ in range(N+1)]
branch_search(giga)
# print(visited)

branch_max_length = max(visited) - 1

print(trunk_length, branch_max_length)
# print(G)

# 12 1
# 1 2 1
# 2 3 2
# 3 4 3
# 4 5 1
# 5 6 2
# 6 7 1
# 5 8 1
# 4 9 2
# 4 10 3
# 10 11 1
# 10 12 2
