# https://www.acmicpc.net/problem/7576

# 방문처리를 언제 할 것인가...?
# 시간초과

from collections import deque
from sys import stdin
from pandas import DataFrame
input = stdin.readline


# def bfs0(v):
#     global chk

#     q0 = deque()
#     q0.append(v)

#     while q0:
#         v = q0.popleft()

#         for d in range(4):
#             new_r = v[0] + dr[d]
#             new_c = v[1] + dc[d]
#             if 0 <= new_r < N and 0 <= new_c < M:
#                 if grid[new_r][new_c] == 0 and not visited0[new_r][new_c]:
#                     visited0[new_r][new_c] = 1
#                     q0.append((new_r, new_c))

#                 if grid[new_r][new_c] == 1:
#                     chk = 1


def bfs(v):
    global chk
    q.append(v)
    # visited[v[0]][v[1]] = 1

    v = q.popleft()
    for d in range(4):
        new_r = v[0] + dr[d]
        new_c = v[1] + dc[d]
        if 0 <= new_r < N and 0 <= new_c < M:
            if grid[new_r][new_c] == 0:
                # visited[new_r][new_c] = 1
                new_spot.append((new_r, new_c))
                grid[new_r][new_c] = 1
                q.append((new_r, new_c))
                chk = True

    # print(DataFrame(grid))
    # break


M, N = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
# print(DataFrame(grid))

visited = [[0 for _ in range(M)] for _ in range(N)]
# visited0 = [[0 for _ in range(M)] for _ in range(N)]

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

# for row in range(N):
#     for col in range(M):
#         if grid[row][col] == 1:
#             visited[row][col] = 1


day = 0
# chk = False
while True:
    chk = False
    new_spot = []           # 오늘 새로 익은 토마토를 담을 리스트
    for row in range(N):
        for col in range(M):
            # if day == 0:
            #     if grid[row][col] == 0:
            #         bfs0((row, col))
            # print('----', day)
            if grid[row][col] == 1 and not visited[row][col]:  # not visited 안해주면 계속 순회
                if (row, col) not in new_spot:                 # 오늘 새로 익은 토마토인지 확인
                    q = deque()
                    # visited[row][col] = 1
                    bfs((row, col))
                    visited[row][col] = 1
                    # print(DataFrame(grid))
                    # print(DataFrame(visited))
                    # chk = True

    if chk:
        day += 1
    else:
        break

if all(sum(grid, start=[])):        # 시간초과
    print(day)
else:
    print(-1)

# print(DataFrame(grid))
# print(DataFrame(visited))
