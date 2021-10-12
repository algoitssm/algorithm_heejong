# https://www.acmicpc.net/problem/15658


def recursive(depth):

    if depth == M:
        print(*ans)
        return
    overlap = 0
    for i in range(N):
        if not visited[i] and overlap != nums[i]:
            ans.append(nums[i])
            visited[i] = 1
            overlap = nums[i]
            recursive(depth+1)
            ans.pop()
            visited[i] = 0


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [0] * N

ans = []
recursive(0)
