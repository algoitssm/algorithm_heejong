# https://www.acmicpc.net/problem/14502
from itertools import combinations
from copy import deepcopy


def dfs(r, c):
    # print(r, c)
    visited[r][c] = 1

    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)

    for i in range(4):
        new_r = r + dr[i]
        new_c = c + dc[i]
        # print(new_r, new_c)
        if 0 <= new_r < N and 0 <= new_c < M:
            if not visited[new_r][new_c] and not grid_case[new_r][new_c]:
                dfs(new_r, new_c)


N, M = map(int, input().split())
lab_grid = []

for _ in range(N):
    lab_grid.append(list(map(int, input().split())))

virus_points = []
empties = []
num_walls = 0

for r in range(N):
    for c in range(M):
        if lab_grid[r][c] == 0:
            empties.append([r, c])

        elif lab_grid[r][c] == 1:
            num_walls += 1          # 벽의 수

        elif lab_grid[r][c] == 2:
            virus_points.append([r, c])

num_walls += 3      # 벽 3개를 더 세우므로
min_sum = N * M

for case in combinations(empties, 3):
    grid_case = deepcopy(lab_grid)

    for case_n in case:
        grid_case[case_n[0]][case_n[1]] = 1

    visited = [[0 for _ in range(M)] for _ in range(N)]

    for virus_point in virus_points:
        row, col = virus_point
        dfs(row, col)

    case_sum = sum(sum(visited, []))

    if min_sum > case_sum:
        min_sum = case_sum

ans = N * M - (min_sum + num_walls)
print(ans)
