# https://www.acmicpc.net/problem/1068


def remove_branches(parent):
    childs = tree[parent]   # 전달되는 노드의 자식들
    tree[parent] = [-1]     # 제거표시. -1 대신 False를 사용하면 tree가 일관되지 않음

    for node in tree:       # 트리 전체를 순회하면서
        if parent in node:  # 전달되는 노드를 자식으로 가지면
            node.remove(parent)  # 제거

    for child in childs:    # 자식들을 순회하면서
        remove_branches(child)  # 재귀


N = int(input())

tree = [[] for _ in range(N)]
input_list = list(map(int, input().split()))

for child, parent in enumerate(input_list):
    if parent == -1:
        continue
    tree[parent].append(child)  # tree: 인덱스 = parent / 값 = child

node_to_remove = int(input())

remove_branches(node_to_remove)
print(tree.count([]))   # 값이 없으면(=[]) leaf node
