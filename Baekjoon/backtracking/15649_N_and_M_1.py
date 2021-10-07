# https://www.acmicpc.net/problem/15649


def perm(depth):

    if depth == M:
        print(*ans)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            ans.append(i+1)
            perm(depth+1)
            visited[i] = 0
            ans.pop()


N, M = map(int, input().split())

nums = [n for n in range(1, N+1)]

ans = []
visited = [0] * N
perm(0)
