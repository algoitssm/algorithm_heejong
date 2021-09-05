# https://www.acmicpc.net/problem/17836
from collections import deque


def bfs(v):
    q = deque()
    q.append(v)

    chk = 0
    while q:

        v = q.popleft()
        row = v[0]
        col = v[1]

        for d in range(4):

            new_r = row + dr[d]
            new_c = col + dc[d]

            if 0 <= new_r < N and 0 <= new_c < M:

                if new_r == N-1 and new_c == M-1:
                    ans.append(visited[row][col]+1)
                    return

                if grid[new_r][new_c] == 0 and not visited[new_r][new_c]:
                    visited[new_r][new_c] = visited[row][col] + 1
                    q.append((new_r, new_c))

                if grid[new_r][new_c] == 2 and chk == 0:
                    chk = 1
                    r_dist = N - 1 - new_r
                    c_dist = M - 1 - new_c
                    ans.append(visited[row][col] + 1 + r_dist + c_dist)


N, M, T = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

visited[0][0] = 1
ans = []
bfs((0, 0))

if ans:
    taken_time = min(ans)-1
else:
    taken_time = -1


if 0 <= taken_time <= T:
    print(taken_time)
else:
    print('Fail')
