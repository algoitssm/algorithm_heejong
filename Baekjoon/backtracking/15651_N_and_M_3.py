# https://www.acmicpc.net/problem/15651


def recursive(depth):

    if depth == M:
        print(*ans)
        return

    for i in range(N):
        ans.append(i+1)
        recursive(depth+1)
        ans.pop()


N, M = map(int, input().split())

nums = [n for n in range(1, N+1)]

ans = []
recursive(0)
