# https://www.acmicpc.net/problem/1967

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(v):
    global max_d

    for n in tree[v[0]]:
        w = n[0]
        d = n[1]
        if visited[w] < 0:
            visited[w] = visited[v[0]] + d
            if visited[w] > max_d:
                max_d = visited[w]
            dfs(n)


n = int(input())
tree = [[] for _ in range(n+1)]    # [자식, 가중치]

for _ in range(n-1):
    p, c, weight = map(int, input().split())
    tree[p].append((c, weight))
    tree[c].append((p, weight))


visited = [-1 for _ in range(n+1)]
max_d = 0
visited[1] = 0
dfs((1, 0))
node = visited.index(max_d)

visited = [-1 for _ in range(n+1)]
max_d = 0
visited[node] = 0
dfs((node, 0))
print(max(visited))
