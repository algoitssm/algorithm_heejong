# https://www.acmicpc.net/problem/7576

# 방문처리를 언제 할 것인가...?

from collections import deque
from sys import stdin
input = stdin.readline


def all_riped(n):
    for row in range(N):
        for col in range(M):
            if grid[row][col] == 0:
                return -1
    return n


M, N = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

day = 0
q = deque()
for row in range(N):
    for col in range(M):
        if grid[row][col] == 1:
            q.append((row, col))

while True:
    chk = False

    q_len = len(q)

    while q_len > 0:
        v = q.popleft()

        for d in range(4):

            new_r = v[0] + dr[d]
            new_c = v[1] + dc[d]

            if 0 <= new_r < N and 0 <= new_c < M:
                if grid[new_r][new_c] == 0:
                    grid[new_r][new_c] = 1
                    q.append((new_r, new_c))
                    chk = True

        q_len -= 1

    if chk:
        day += 1
    else:
        break

print(all_riped(day))

# if all(sum(grid, start=[])):
#     print(day)
# else:
#     print(-1)
