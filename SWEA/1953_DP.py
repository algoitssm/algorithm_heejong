import sys
# from collections import deque
sys.stdin = open('input4.txt')

# 우하좌상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],  # 상하좌우
    [0, 1, 0, 1],  # 상하
    [1, 0, 1, 0],  # 좌우
    [1, 0, 0, 1],  # 상우
    [1, 1, 0, 0],  # 하우
    [0, 1, 1, 0],  # 하좌
    [0, 0, 1, 1],  # 상좌
]


for tc in range(int(input())):
    # 지도 세로, 지도 가로, 뚜껑 세로, 뚜껑 가로, 시간
    N, M, R, C, L = map(int, input().split())

    G = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    q = [(R, C)]
    visited[R][C] = 1

    ans = 0

    while q:
        r, c = q.pop(0)
        ans += 1

        if visited[r][c] >= L:
            continue

        # 4방향 탐색
        for d in range(4):
            curr_p = G[r][c]

            # 현재 바라보는 방향으로 길이 없으면
            if pipe[curr_p][d] == 0:
                continue

            nr = r + dr[d]
            nc = c + dc[d]

            # 맵 범위
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            nd = (d+2) % 4
            np = G[nr][nc]

            # 방문을 했거나, 다음 좌표의 파이프가 현 좌표와 연결되지 않는다면
            if visited[nr][nc] or pipe[np][nd] == 0:
                continue

            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))

    print('#{0} {1}'.format(tc+1, ans))
    # break
