import sys
sys.stdin = open('input.txt')

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


def connect_line(v):
    visited[v[0]][v[1]] = 1

    n_row = v[0] + dr[d]
    n_col = v[1] + dc[d]
    if 0 <= n_row < N and 0 <= n_col < N:
        if not visited[n_row][n_col]:
            connect_line((n_row, n_col), d)
        else:   # 전선이나 코어를 만난 경우
            return
    else:       # 연결성공
        return

    visited[v[0]][v[1]] = 0

def set_field(k):

    for r in range(N):
        for c in range(N):
            if G[r][c] == 1:

                for 
                connect_line((r,c))

for tc in range(int(input())):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    cores_num = sum(sum(G, []))
    # print(cores_num)

    k = cores_num

    max_cnt = 0
    min_len = N*N

    while k > 0:
        visited = [[0 for _ in range(N)] for _ in range(N)]

        set_field(k)    # depth 전달

        # for row in range(N):
        #     for col in range(N):
        #         if G[row][col] == 1:
        #             for d in range(4):
        #                 connect_core((row, col), d)   # core좌표, 방향변수

        if min_len != N*N:
            break

        k -= 1

    # for r in range(N):
    #     for c in range(N):
    #         cnt = length = 0

    #         if G[r][c] == 1:
    #             dfs((r,c))

    #         if max_cnt <= cnt:
    #             max_cnt = cnt
    #             if min_len > length:
    #                 min_len = length

    print('#{} {}'.format(tc+1, min_len))
    break
