# https://www.acmicpc.net/problem/6416

def dfs1(r):
    cycle_check[r] = 1

    for child in tree[r]:
        if cycle_check[child]:
            return False

    return True


def dfs2(r):
    visited[r] = 1

    for child in tree[r]:
        if not visited[child]:
            dfs2(child)
        # pass


tc = 1
while True:
    try:
        nodes = []
        chk = True

        while True:
            nodes += list(map(int, input().split()))
            if 0 in nodes:
                break

        N = len(nodes)
        max_node = max(nodes)
        tree = [[] for _ in range(max_node + 1)]    # [child, parent]
        connected_node = [[0, 0]
                          for _ in range(max_node + 1)]  # [child 수, parent 수]

        for i in range(0, N, 2):
            tree[nodes[i]].append(nodes[i+1])
            connected_node[nodes[i]][0] += 1
            connected_node[nodes[i+1]][1] += 1

        root = []
        for j in range(max_node+1):
            if connected_node[j][0] and not connected_node[j][1]:   # 자식은 있고 부모가 없으면
                root.append(j)                                      # 루트

        if len(root) > 1:           # 루트가 2개 이상일 경우
            print('1111')
            chk = False

        if chk:
            for node in connected_node:
                if node[1] > 1:         # 부모가 둘 이상이면
                    print('2222')
                    chk = False
                    break

        if chk:
            cycle_check = [0 for _ in range(max_node+1)]
            chk = dfs1(root[0])

        if chk:
            visited = [0 for _ in range(max_node+1)]    # 하나의 루트로 전부 탐색하지 못할 경우
            dfs2(root[0])
            print(visited)
            for k in range(1, max_node+1):
                if not connected_node[0] or not connected_node[1]:
                    if not visited[k]:
                        print('3333')
                        chk = False
                        break

        nxt_input = map(int, input().split())

        if chk:
            print('Case {} is a tree.'.format(tc))
        else:
            print('Case {} is not a tree.'.format(tc))

        # if nxt_input != []:
        #     break

        tc += 1

    except:
        break
