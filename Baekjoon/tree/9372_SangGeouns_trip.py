# https://www.acmicpc.net/problem/9372
import sys
input = sys.stdin.readline  # 이거 없으면 시간초과


def dfs(v, cnt):
    # global cnt
    visited[v] = 1
    # cnt += 1

    for w in G[v]:
        if not visited[w]:
            cnt += 1
            cnt = dfs(w, cnt)

    return cnt


T = int(input())

while T > 0:
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # print(G)
    visited = [0 for _ in range(N+1)]

    cnt = 0
    print(dfs(1, cnt))

    T -= 1
