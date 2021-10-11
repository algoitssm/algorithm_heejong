# https://www.acmicpc.net/problem/15657


def recursive(depth, k):

    if depth == M:
        print(*ans)
        return

    for i in range(k, N):
        ans.append(nums[i])
        recursive(depth+1, i)
        ans.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [0] * N

ans = []
recursive(0, 0)
