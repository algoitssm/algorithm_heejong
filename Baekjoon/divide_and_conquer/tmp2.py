import sys
sys.stdin = open('input.txt')

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


def connect(v, direction, cnt):  # 좌표, 방향

    global temp_ans

    n_row = v[0] + dr[direction]
    n_col = v[1] + dc[direction]

    if n_row < 0 or n_row >= N or n_col < 0 or n_col >= N:
        # print(visited)
        if temp_ans > cnt:
            temp_ans = cnt
        return

    if G[n_row][n_col] == 1:
        return

    connect((n_row, n_col), direction, cnt+1)


for tc in range(int(input())):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    cores_num = sum(sum(G, []))
    visited = [[0] * N for _ in range(N)]
    accum_ans = 0

    i = 0
    while i < (N//2 + N % 2):
        side_sum = 0

        for c in range(N):

            if not visited[i][c] and G[i][c] == 1:
                temp_ans = 9999
                possible_direction = [0, 1, 3]
                for d in possible_direction:
                    connect((i, c), d, 0)   # 좌표, 방향, 누적
                side_sum += temp_ans
                print('temp_ans: ', temp_ans)

            if not visited[N-(i+1)][N-(c+1)] and G[N-(i+1)][N-(c+1)] == 1:
                temp_ans = 9999
                possible_direction = [0, 1, 2]
                for d in possible_direction:
                    connect((i, c), d, 0)   # 좌표, 방향, 누적
                side_sum += temp_ans

        for r in range(N):

            if not visited[r][i] and G[r][i] == 1:
                temp_ans = 9999
                possible_direction = [1, 2, 3]
                for d in possible_direction:
                    connect((i, c), d, 0)   # 좌표, 방향, 누적
                side_sum += temp_ans

            if not visited[N-(r+1)][N-(i+1)] and G[N-(r+1)][N-(i+1)] == 1:
                temp_ans = 9999
                possible_direction = [0, 2, 3]
                for d in possible_direction:
                    connect((i, c), d, 0)   # 좌표, 방향, 누적
                side_sum += temp_ans

        accum_ans += side_sum
        print(accum_ans)
        i += 1
        print('----')

    print('#{} {}'.format(tc+1, accum_ans))
    break
