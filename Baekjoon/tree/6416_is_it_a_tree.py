# https://www.acmicpc.net/problem/6416

# Unsolved
# 트리인지 판단하는 기준을 4가지로 생각
# 1. 루트가 없을경우 / 2. 부모가 둘 이상인 자식이 있을 경우
# 3. 사이클이 존재할 경우 / 4. 하나의 루트로 전부 순회하지 못했을 경우

import sys
input = sys.stdin.readline


def dfs(r):
    global chk
    global cnt

    cycle_check[r] = 1
    cnt += 1

    for child in tree[r]:
        if not cycle_check[child]:
            dfs(child)
        else:           # 이미 사이클로 지난 노드를 만나면
            chk = False  # 트리 아님

    return cnt


tc = 1
while True:
    input_data = []  # 입력으로 받을 리스트
    nodes = []      # 노드의 번호를 담을 리스트
    chk = True

    while True:
        input_data += list(map(int, input().split()))
        if 0 in input_data:  # 0이 입력되면
            break           # 끝

    N = len(input_data)
    max_node = max(input_data)

    tree = [[] for _ in range(max_node + 1)]    # [child, parent]
    connected_node = [[0, 0]
                      for _ in range(max_node + 1)]  # [child 수, parent 수] : 노드별로 개수에 관한 리스트

    for i in range(0, N, 2):        # 두 칸씩 띄어서 입력
        m = input_data[i]
        n = input_data[i+1]
        tree[m].append(n)
        connected_node[m][0] += 1   # child 수 += 1
        connected_node[n][1] += 1   # parent 수 += 1

        nodes.append(m)         # nodes 리스트에 해당 번호를 담는다
        nodes.append(n)

    nodes = sorted(list(set(nodes)))    # 중복을 제거. 0을 앞으로 빼기 위해 정렬

    root = 0
    for node in nodes:
        if connected_node[node][0] and not connected_node[node][1]:  # 자식은 있고 부모가 없으면
            root = node                                             # 루트

    if not root:    # 루트가 나오지 않았을 경우
        chk = False

    if chk:
        for edges in connected_node:
            if edges[1] > 1:        # 부모가 둘 이상이면
                chk = False         # 트리 X
                break

    # print('-----')
    # 사이클이 있을 경우
    if chk:
        cycle_check = [0 for _ in range(max_node+1)]
        cnt = 0
        dfs(root)

        # print(cnt, N)

        # print(cnt)

        if cnt < N//2:
            chk = False

    # 하나의 루트로 다 순회하지 못했을 경우
    # if chk:
    #     for node in nodes[1:]:         # 0 빼고 순회
    #         if not cycle_check[node]:
    #             chk = False
    #             break

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
