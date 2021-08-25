# https://www.acmicpc.net/problem/2178
from collections import deque


def bfs(r, c):
    dq = deque()
    dq.append((r, c))
    visited[r][c] = 1

    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)

    while dq:
        r, c = dq.popleft()

        for d in range(4):
            new_r = r + dr[d]
            new_c = c + dc[d]
            if 0 <= new_r < N and 0 <= new_c < M:
                if maze[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                    visited[new_r][new_c] = visited[r][c] + 1
                    dq.append((new_r, new_c))
    return visited[N-1][M-1]


N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

visited = [[0 for _ in range(M)] for _ in range(N)]
ans = bfs(0, 0)
print(ans)
