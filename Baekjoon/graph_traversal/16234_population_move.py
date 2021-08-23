# https://www.acmicpc.net/problem/16234

# Runtime Error


def dfs(row, col):
    global cnt
    global total_pop
    visited[row][col] = area_num
    # print('r, c: ', row, col)
    # print('cnt, total_pop: ', cnt, total_pop)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for d in range(4):
        new_r = row + dr[d]
        new_c = col + dc[d]
        if 0 <= new_r < N and 0 <= new_c < N:
            if L <= abs(A[new_r][new_c] - A[row][col]) <= R:
                if not visited[new_r][new_c]:
                    cnt += 1
                    total_pop += A[new_r][new_c]
                    # print(cnt, total_pop)
                    dfs(new_r, new_c)


N, L, R = map(int, input().split())
A = []

for _ in range(N):
    A.append(list(map(int, input().split())))

day = 0

while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]

    chk = 0
    area_num = 1
    for grid_r in range(N):
        for grid_c in range(N):
            if not visited[grid_r][grid_c]:
                cnt = 1
                total_pop = A[grid_r][grid_c]
                dfs(grid_r, grid_c)

                if cnt > 1:

                    refreshed_pop = total_pop // cnt
                    # print(refreshed_pop)
                    for r in range(N):
                        for c in range(N):
                            if visited[r][c] == area_num:
                                A[r][c] = refreshed_pop
                    # print('A: ', A)
                    chk = 1

                area_num += 1

    # print(visited)
    if chk == 0:
        break
    day += 1
# print(A)
print(day)
