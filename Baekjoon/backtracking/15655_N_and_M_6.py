# https://www.acmicpc.net/problem/15655


def recursive(depth, k):

    if depth == M:
        print(*ans)
        return

    for i in range(k, N):
        if not visited[i]:
            ans.append(nums[i])
            visited[i] = 1
            recursive(depth+1, i)
            ans.pop()
            visited[i] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [0] * N

ans = []
recursive(0, 0)
