import sys
sys.stdin = open('input14.txt')


def guard_area(v, k):
    global ans

    row = v[0]
    col = v[1]

    cnt = 0
    for r in range(N):
        for c in range(N):
            if G[r][c]:
                if abs(row-r) + abs(col-c) < k:
                    cnt += 1

    if M * cnt >= k**2 + (k-1)**2:
        return cnt
    return 0


for tc in range(int(input())):
    N, M = map(int, input().split())
    G = [tuple(map(int, input().split())) for _ in range(N)]

    k = 2*N - 1
    # k = N + 2

    ans = 0
    while not ans:

        for row in range(N):
            for col in range(N):
                ans = max(guard_area((row, col), k), ans)

        k -= 1

    print('#{0} {1}'.format(tc+1, ans))
    # break
