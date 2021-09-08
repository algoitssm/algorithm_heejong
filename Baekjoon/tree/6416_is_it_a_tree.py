# https://www.acmicpc.net/problem/6416

# Unsolved

import sys
input = sys.stdin.readline


def dfs(r):
    global chk

    cycle_check[r] = 1

    for child in tree[r]:
        if not cycle_check[child]:
            dfs(child)
        else:
            chk = False

    return


tc = 1
while True:
    input_data = []
    nodes = []
    chk = True

    while True:
        input_data += list(map(int, input().split()))
        if 0 in input_data:
            break

    N = len(input_data)
    max_node = max(input_data)

    tree = [[] for _ in range(max_node + 1)]    # [child, parent]
    connected_node = [[0, 0]
                      for _ in range(max_node + 1)]  # [child 수, parent 수]

    for i in range(0, N, 2):
        m = input_data[i]
        n = input_data[i+1]
        tree[m].append(n)
        connected_node[m][0] += 1
        connected_node[n][1] += 1

        if m not in nodes:
            nodes.append(m)
        if n not in nodes:
            nodes.append(n)

    root = 0
    for node in nodes:
        if connected_node[node][0] and not connected_node[node][1]:  # 자식은 있고 부모가 없으면
            root = node                                             # 루트

    if not root:           # 루트가 나오지 않았을 경우
        chk = False

    if chk:
        for edges in connected_node:
            if edges[1] > 1:         # 부모가 둘 이상이면
                chk = False
                break

    # 사이클이 있을 경우
    if chk:
        cycle_check = [0 for _ in range(max_node+1)]
        dfs(root)

    # 하나의 루트로 다 순회하지 못했을 경우
    if chk:
        for node in nodes[:-1]:
            if not cycle_check[node]:
                chk = False
                break

    nxt_input = input().split()

    if chk:
        print('Case {} is a tree.'.format(tc))
    else:
        print('Case {} is not a tree.'.format(tc))

    tc += 1

    if nxt_input == []:
        continue

    if int(nxt_input[0]) < 0 and int(nxt_input[1]) < 0:
        break
