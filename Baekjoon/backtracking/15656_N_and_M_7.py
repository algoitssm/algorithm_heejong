# https://www.acmicpc.net/problem/15656


def recursive(depth):

    if depth == M:
        print(*ans)
        return

    for i in range(N):
        ans.append(nums[i])
        recursive(depth+1)
        ans.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [0] * N

ans = []
recursive(0)
