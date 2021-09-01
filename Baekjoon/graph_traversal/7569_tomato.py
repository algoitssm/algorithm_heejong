# https://www.acmicpc.net/problem/7569

# Python 3 TimeError
# PyPy 3 Solved

from collections import deque
from sys import stdin
# from pandas import DataFrame
input = stdin.readline


def all_riped(n):
    for height in range(H):
        for row in range(N):
            for col in range(M):
                if grid[height][row][col] == 0:
                    return -1
    return n


M, N, H = map(int, input().split())

grid = []
for _ in range(H):
    floor_grid = []
    for _ in range(N):
        floor_grid.append(list(map(int, input().split())))
    grid.append(floor_grid)

# print(grid)
# 북 동 남 서 상 하
dr = (-1, 0, 1, 0, 0, 0)
dc = (0, 1, 0, -1, 0, 0)
dh = (0, 0, 0, 0, 1, -1)

day = 0
q = deque()
for height in range(H):
    for row in range(N):
        for col in range(M):
            if grid[height][row][col] == 1:
                q.append((height, row, col))


while True:
    chk = False

    q_len = len(q)

    while q_len > 0:
        v = q.popleft()

        for r, c, h in zip(dr, dc, dh):

            new_h = v[0] + h
            new_r = v[1] + r
            new_c = v[2] + c

        # for d in range(6):

            # new_h = v[0] + dh[d]
            # new_r = v[1] + dr[d]
            # new_c = v[2] + dc[d]

            if 0 <= new_h < H and 0 <= new_r < N and 0 <= new_c < M:
                new_spot = grid[new_h][new_r][new_c]
                if new_spot == 0:
                    grid[new_h][new_r][new_c] = 1
                    q.append((new_h, new_r, new_c))
                    chk = True

        q_len -= 1

    if chk:
        day += 1
    else:
        break

print(all_riped(day))
