# https://www.acmicpc.net/problem/16918
from pandas import DataFrame


def boom(grid):

    new_grid = [['O' for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':
                new_grid[r][c] = '.'

                for d in range(4):
                    new_r = r + dr[d]
                    new_c = c + dc[d]

                    if 0 <= new_r < R and 0 <= new_c < C:
                        new_grid[new_r][new_c] = '.'

    return new_grid


R, C, N = map(int, input().split())

first_grid = [list(input()) for _ in range(R)]

# print(DataFrame(grid))

# boomed_grid = [['O' for _ in range(C)] for _ in range(R)]


dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

third_grid = boom(first_grid)
fifth_grid = boom(third_grid)

# for r in range(R):
#     for c in range(C):
#         if first_grid[r][c] == 'O':
#             boomed_grid[r][c] = '.'

#             for d in range(4):
#                 new_r = r + dr[d]
#                 new_c = c + dc[d]

#                 if 0 <= new_r < R and 0 <= new_c < C:
#                     boomed_grid[new_r][new_c] = '.'

# if boomed_grid == [['.' for _ in range(C)] for _ in range(R)]:
#     odd_grid
# print(DataFrame(boomed_grid))

if N == 1:
    for k in range(R):
        print(''.join(first_grid[k]))

else:
    if N % 4 == 1:
        for k in range(R):
            print(''.join(fifth_grid[k]))
    elif N % 4 == 3:
        for k in range(R):
            print(''.join(third_grid[k]))
    else:
        for k in range(R):
            print('O' * C)
