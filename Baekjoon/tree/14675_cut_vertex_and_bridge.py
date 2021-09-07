# https://www.acmicpc.net/problem/14675
import sys
from copy import deepcopy
input = sys.stdin.readline


def dfs(v):
    visited[v] = 1

    for child in new_tree[v]:
        if not visited[child]:
            dfs(child)


def are_they_connected(lst):
    v = lst[0]

    dfs(v)

    my_sum = 0
    for node in lst:
        my_sum += visited[node]

    if my_sum == len(lst):
        return True
    return False


def cut_vertex(k):

    for e in new_tree:
        if k in e:
            e.remove(k)

    check = new_tree[k]

    return are_they_connected(check)


def cut_bridge(k):

    n1, n2 = bridge_tag[k-1]
    new_tree[n1].remove(n2)
    new_tree[n2].remove(n1)

    return are_they_connected((n1, n2))


N = int(input())

tree = [[] for _ in range(N+1)]
bridge_tag = []
for _ in range(N-1):
    p, c = map(int, input().split())
    tree[p].append(c)
    tree[c].append(p)
    bridge_tag.append((p, c))

# print(tree)
q = int(input())

for _ in range(q):
    new_tree = deepcopy(tree)
    t, k = map(int, input().split())
    visited = [0 for _ in range(N+1)]

    if t == 1:
        chk = cut_vertex(k)   # 입력으로 주어지는 정보는 트리임이 보장되므로 check는 무조건 존재
    elif t == 2:
        chk = cut_bridge(k)

    if chk:
        print('no')
    else:
        print('yes')
