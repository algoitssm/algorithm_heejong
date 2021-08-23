# https://www.acmicpc.net/problem/1325
# TimeError
import sys
input = sys.stdin.readline


def dfs(v):
    # print('------')
    global cnt
    cnt += 1
    visited[v] = 1

    # if cnt_list[v]:
    #     return cnt + cnt_list[v]

    for edge in G[v]:
        if edge and not visited[edge]:
            dfs(edge)

    return cnt


N, M = map(int, input().split())

G = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    G[e].append(s)

# print(G)

max_cnt = 0
cnt_list = [0 for _ in range(N+1)]
# cnt_dict = {}

for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    cnt = 0
    cnt = dfs(i)
    if max_cnt < cnt:
        max_cnt = cnt
    cnt_list[i] = cnt
    # cnt_dict[i] = cnt

print(max_cnt)

for idx, val in enumerate(cnt_list):
    if val == max_cnt:
        print(idx, end=' ')

# for key, val in cnt_dict.items():
#     if val == max_cnt:
#         print(key, end=' ')
print()
