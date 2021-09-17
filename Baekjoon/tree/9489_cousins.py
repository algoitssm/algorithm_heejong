# https://www.acmicpc.net/problem/9489

while True:
    n, k = map(int, input().split())

    if not n and not k:
        break

    nodes = list(map(int, input().split()))

    parent = [[] for _ in range(n+1)]
    childs = [[] for _ in range(n+1)]

    for node in nodes:
        pass

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
    # print(G)

    # while idx < len(G):

    #     idx += 1
