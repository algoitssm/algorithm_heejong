# https://www.acmicpc.net/problem/15665


def recursive(depth):

    if depth == M:
        print(*ans)
        return

    overlap = 0
    for i in range(N):
        if overlap != nums[i]:
            ans.append(nums[i])
            overlap = nums[i]
            recursive(depth+1)
            ans.pop()


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

# visited = [0] * N

ans = []
recursive(0)
