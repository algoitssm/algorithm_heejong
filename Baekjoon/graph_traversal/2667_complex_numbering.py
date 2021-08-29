# https://www.acmicpc.net/problem/2667
# from pandas import DataFrame


def dfs(v):
    global cnt
    row = v[0]
    col = v[1]

    for d in range(4):
        new_row = row + dr[d]
        new_col = col + dc[d]
        if 0 <= new_row < N and 0 <= new_col < N:
            if grid[new_row][new_col] == 1:
                if not visited[new_row][new_col]:
                    visited[new_row][new_col] = cnt
                    dfs((new_row, new_col))
                    cnt += 1

    return cnt


N = int(input())

grid = []
for _ in range(N):
    grid.append(list(map(int, input())))
# print(grid)

visited = [[0 for _ in range(N)] for _ in range(N)]
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

section = 0
cnt_list = list()
for r in range(N):
    for c in range(N):
        if grid[r][c] and not visited[r][c]:
            cnt = 1
            visited[r][c] = cnt
            result = dfs((r, c))
            section += 1
            cnt_list.append(result)

# print(DataFrame(visited))
cnt_list.sort()         # 이거 빼먹어서 계속 틀림
print(section)
for count in cnt_list:
    print(count)
