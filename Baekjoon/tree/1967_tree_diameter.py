# https://www.acmicpc.net/problem/1967
# TimeError

import sys
from itertools import combinations
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def find_distance(a, b, cum):
    global total

    if a == b:
        total += cum
        return

    visited[a] = 1

    for c in tree[a]:
        if not visited[c[0]]:
            cum += c[1]
            find_distance(c[0], b, cum)
            cum -= c[1]


n = int(input())
tree = [[] for _ in range(n+1)]    # [자식, 가중치]

for _ in range(n-1):
    p, c, weight = map(int, input().split())
    tree[p].append((c, weight))
    tree[c].append((p, weight))

# print(tree)

for temp in range(n, 1, -1):        # chk 부터 leaf node
    if len(tree[temp]) > 1:
        chk = temp + 1
        break

# 한 leaf node에서 시작
leaf_node_list = [k for k in range(chk, n+1)]
# print(leaf_node_list)

K = n + 1 - chk   # leaf node 개수

# my_max = 0
# for i in range(K):      # 2개 뽑는 조합
#     for j in range(i+1, K):
#         visited = [0 for _ in range(n+1)]
#         total = 0
#         find_distance(leaf_node_list[i], leaf_node_list[j], 0)
#         if my_max < total:
#             my_max = total

my_max = 0
for points in combinations(leaf_node_list, 2):
    visited = [0 for _ in range(n+1)]
    total = 0
    find_distance(points[0], points[1], 0)
    if my_max < total:
        my_max = total

print(my_max)
