# https://www.acmicpc.net/problem/9489
# Google Helped me

from collections import defaultdict


while True:
    n, k = map(int, input().split())

    if not n:
        break

    nodes = list(map(int, input().split()))

    # if k == nodes[0]:
    #     print(0)
    #     continue

    G, level = defaultdict(list), {}
    cur_p = 0   # nodes에서 현재 index
    G[0], level[nodes[cur_p]] = [nodes[cur_p]], 0  # G는 트리, level는 노드별 레벨 저장
    # print(dict(G), level)

    for i in range(1, n):
        # print('cur_p:', cur_p)
        # print('nodes[cur_p]:', nodes[cur_p])
        # print(G[nodes[cur_p]])
        if G[nodes[cur_p]] != []:
            if nodes[i] != G[nodes[cur_p]][-1] + 1:
                cur_p += 1
        G[nodes[cur_p]].append(nodes[i])
        level[nodes[i]] = nodes[cur_p]
        # print(dict(G), level)

    ans = 0
    for p in G[level[level[k]]]:
        if p != level[k]:
            ans += len(G[p])

    print(ans)
    # break

    # tmp = nodes[0]
    # G = []
    # tmp_list = []

    # for node in nodes:

    #     if tmp == node - 1:
    #         tmp_list.append(node)
    #     else:
    #         G.append(tmp_list)
    #         tmp_list = []
    #         tmp_list.append(node)
    #     tmp = node

    # if tmp_list:
    #     G.append(tmp_list)

    # G.pop(0)
    # G.pop(0)

    # tree = [[] for _ in range(max(nodes)+1)]

    # idx = 0
    # level = []
    # for childs in G:
    #     print(nodes[idx])
    #     tree[nodes[idx]] = childs
    #     idx += 1

    # print(tree)

    # while idx < len(G):

    #     idx += 1
