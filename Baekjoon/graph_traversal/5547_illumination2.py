# https://www.acmicpc.net/problem/5547

from pandas import DataFrame


def dfs(v):
    row = v[0]
    col = v[1]
    # print(row, col)

    if row & 1:
        up_building = buildings[row//2][col]
        down_left_building = 0
        down_right_building = 0

        if row // 2 + 1 < H:
            down_left_building = buildings[row//2 + 1][col - 1]
            down_right_building = buildings[row//2 + 1][col]

        if 0 < up_building + down_left_building + down_right_building < 3:
            if not dot_grid[row][col]:
                print(row, col)
                dot_grid[row][col] = 1
                dfs((row - 1, col))
                if not (row//2) & 1:
                    # print('----')
                    dfs((row - 1, col - 1))
                if row < dot_H:
                    dfs((row + 1, col))

    else:
        up_left_building = 0
        up_right_building = 0
        down_building = buildings[row//2 + 1][col]

        if row > 0:
            up_left_building = buildings[row//2][col - 1]
            up_right_building = buildings[row//2][col]

        if up_right_building + down_building == 1:
            dot_grid[row][col] = 1

            if not dot_grid[row+1][col+1]:
                dfs((row+1, col+1))

        if row//2 & 1 > 0:
            if up_left_building + down_building == 1:

                dfs((row + 1, col))

        if 0 < up_left_building + up_right_building + down_building < 3:
            if not dot_grid[row][col]:
                print(row, col)
                # print(row, col, ':', up_left_building,
                #       up_right_building, down_building)
                dot_grid[row][col] = 1
                dfs((row + 1, col + 1))
                if row//2 & 1 > 0:
                    dfs((row + 1, col))
                if row > 0:
                    dfs((row - 1, col))


W, H = map(int, input().split())

buildings = [[0 for _ in range(W+1)]] + [[0] +
                                         list(map(int, input().split())) for _ in range(H)]

# print(buildings)
# print(DataFrame(buildings))

dot_W = W + 1
dot_H = H * 2 + 2
dot_grid = [[0 for _ in range(dot_W)] for _ in range(dot_H)]
# visited = [[0 for _ in range(dot_W)] for _ in range(dot_H)]

for r in range(dot_H):
    for c in range(dot_W):
        # if
        point = (r, c)
        dfs(point)


# print(DataFrame(buildings))


# print(cul_sum)
# print(DataFrame(visited))
