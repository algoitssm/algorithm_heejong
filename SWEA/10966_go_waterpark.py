from collections import deque
import sys
sys.stdin = open('input5.txt')

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

for tc in range(int(input())):

    N, M = map(int, input().split())    # N 세로, M 가로
    arr = [input() for _ in range(N)]
    dist = [[987654321] * M for _ in range(N)]  # 방문 및 거리 체크

    # q = deque()

    q = [0] * M * N
    front = -1
    rear = -1
    print(q)

    for i in range(N):      # 시작점인 물을 몽땅 담자
        for j in range(M):
            if arr[i][j] == 'W':
                # q.append((i, j))
                rear += 1
                q[rear] = (i, j)
                dist[i][j] = 0

    while front != rear:
        # r, c = q.popleft()
        front += 1
        r, c = q[front]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if arr[nr][nc] == 'L' and dist[nr][nc] == 987654321:
                dist[nr][nc] = dist[r][c] + 1
                # q.append((nr, nc))
                rear += 1
                q[rear] = (nr, nc)

    print(q)
    ans = 0

    for i in dist:
        for j in i:
            ans += j
    print('#{0} {1}'.format(tc+1, ans))
    # break
