# https://www.acmicpc.net/problem/5547
from pandas import DataFrame


def dfs(spot):
    global light, connected

    row, col = spot[0], spot[1]
    visited[row][col] = 1

    # 같은 행 오른쪽
    new_col1 = col + 1

    if new_col1 < W:

        new_spot1 = (row, new_col1)

        if buildings[row][new_col1]:
            connected += 1
            if not visited[row][new_col1]:
                light += 1
                dfs(new_spot1)

    # y가 홀수일 때, x, x+1 (= 인덱스는 하나 작아서 row가 짝수일 때)
    if not row % 2:
        new_row = row + 1
        new_col2 = col
        new_col3 = col + 1

        if new_row < H:
            new_spot2 = (new_row, new_col2)

            if buildings[new_row][new_col2]:
                connected += 1
                if not visited[new_row][new_col2]:
                    light += 1
                    dfs(new_spot2)

            if new_col3 < W:
                new_spot3 = (new_row, new_col3)

                if buildings[new_row][new_col3]:
                    connected += 1
                    if not visited[new_row][new_col3]:
                        light += 1
                        dfs(new_spot3)

    # y가 짝수일 때, x-1, x (row가 홀수일 때)
    else:
        new_row = row + 1
        new_col2 = col - 1
        new_col3 = col

        if new_row < H:

            if new_col3 >= 0:
                new_spot2 = (new_row, new_col2)

                if buildings[new_row][new_col2]:
                    connected += 1
                    if not visited[new_row][new_col2]:
                        light += 1
                        dfs(new_spot2)

            new_spot3 = (new_row, new_col3)

            if buildings[new_row][new_col3]:
                connected += 1
                if not visited[new_row][new_col3]:
                    light += 1
                    dfs(new_spot3)


W, H = map(int, input().split())

buildings = [list(map(int, input().split())) for _ in range(H)]

print(DataFrame(buildings))

visited = [[0 for _ in range(W)] for _ in range(H)]

cul_sum = 0
for r in range(H):
    for c in range(W):
        # print(r, c)
        # light = 0
        # connected = 0
        if buildings[r][c] == 1 and not visited[r][c]:
            connected = 0
            light = 1
            building = (r, c)
            dfs(building)
            # print(r, c)
            cul_sum += 6 * light - 2 * connected
            # print(light, connected)
            # break

print(cul_sum)
# print(DataFrame(visited))
