# https://www.acmicpc.net/problem/15650


def recursive(depth, k):

    if depth == M:
        print(*ans)
        return

    for i in range(k, N):
        if not visited[i]:
            visited[i] = 1
            ans.append(i+1)
            recursive(depth+1, i)
            visited[i] = 0
            ans.pop()


N, M = map(int, input().split())

nums = [n for n in range(1, N+1)]

ans = []
visited = [0] * N
recursive(0, 0)
