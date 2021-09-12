# https://www.acmicpc.net/problem/15900
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(v, cnt):
    global ans

    # leaf node일 경우 ans에 누적
    if v != 1 and not visited[v] and len(tree[v]) == 1:
        ans += cnt
        return

    visited[v] = 1

    for w in tree[v]:
        if not visited[w]:
            cnt += 1
            dfs(w, cnt)
            cnt -= 1        # 이게 포인트


N = int(input())

tree = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
# print(tree)
ans = 0
dfs(1, 0)

# print(ans)
if ans & 1:
    print('Yes')
else:
    print('No')
