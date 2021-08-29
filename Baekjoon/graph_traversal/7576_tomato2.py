# https://www.acmicpc.net/problem/7576

# 방문처리를 언제 할 것인가...?

from collections import deque
from sys import stdin
from pandas import DataFrame
input = stdin.readline


def bfs(v):
    global chk
    q2 = deque()

    q.append(v)
    visited[v[0]][v[1]] = day + 1

    v = q.popleft()
    for d in range(4):
        new_r = v[0] + dr[d]
        new_c = v[1] + dc[d]
        if 0 <= new_r < N and 0 <= new_c < M:
            if grid[new_r][new_c] == 0:
                visited[new_r][new_c] = visited[v[0]][v[1]] + 1
                grid[new_r][new_c] = 1
                q.append((new_r, new_c))
                chk = True


M, N = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

visited = [[0 for _ in range(M)] for _ in range(N)]

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

day = 0
q = deque()
while True:
    chk = False
    for row in range(N):
        for col in range(M):
            if grid[row][col] == 1 and not visited[row][col]:
                bfs((row, col))

    if chk:
        day += 1
    else:
        break

if all(sum(grid, start=[])):
    print(day)
else:
    print(-1)

print(DataFrame(grid))
print(DataFrame(visited))
