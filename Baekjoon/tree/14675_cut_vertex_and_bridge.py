# https://www.acmicpc.net/problem/14675

import sys
# from copy import deepcopy
# from collections import deque
input = sys.stdin.readline

# 트리가 아니라 그래프가 주어질 경우 판단
# def bfs(v, lst, n):
#     cnt = 1
#     q = deque()
#     q.append(v)

#     visited[v] = 1

#     while q:

#         if cnt == n:
#             return True

#         v = q.popleft()

#         for child in new_tree[v]:
#             if not visited[child]:
#                 q.append(child)
#                 if child in lst:
#                     cnt += 1

#     return False


# def are_they_connected(lst):
#     v = lst[0]
#     n = len(lst)
#     return bfs(v, lst, n)


# def cut_vertex(k):

#     for e in new_tree[k]:
#         new_tree[e].remove(k)

#     check = new_tree[k]

#     return are_they_connected(check)


# def cut_bridge(k):

#     n1, n2 = bridge_tag[k-1]
#     new_tree[n1].remove(n2)
#     new_tree[n2].remove(n1)

#     return are_they_connected((n1, n2))


# N = int(input())

# tree = [[] for _ in range(N+1)]
# bridge_tag = []
# for _ in range(N-1):
#     p, c = map(int, input().split())
#     tree[p].append(c)
#     tree[c].append(p)
#     bridge_tag.append((p, c))

# # print(tree)
# q = int(input())

# for _ in range(q):
#     new_tree = deepcopy(tree)
#     t, k = map(int, input().split())
#     visited = [0 for _ in range(N+1)]

#     if t == 1:
#         chk = cut_vertex(k)   # 입력으로 주어지는 정보는 트리임이 보장되므로 check는 무조건 존재
#     elif t == 2:
#         chk = cut_bridge(k)

#     if chk:
#         print('no')
#     else:
#         print('yes')


N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, c = map(int, input().split())
    tree[p].append(c)
    tree[c].append(p)

q = int(input())

for _ in range(q):
    chk = True
    t, k = map(int, input().split())

    if t == 1:          # 점일 때
        if len(tree[k]) == 1:   # 연결된 간선이 하나이면
            chk = False  # 단절점 아님
    # elif t == 2:      # 간선일 때
    #     chk = True    # 무조건 단절선

    if chk:
        print('yes')
    else:
        print('no')
