# https://www.acmicpc.net/problem/15681

import sys
from collections import deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def remove_parent(v):   # 부모 제거 함수
    visited[v] = 1

    for w in G[v]:
        if not visited[w]:
            remove_parent(w)    # 계속 재귀
            G[w].remove(v)      # 현재 노드에서 부모 제거


def count_node(v):

    node_cnt = node_cnt_list[v]
    if node_cnt:            # 이미 셌던 노드면
        return node_cnt     # 그 숫자 반환

    if not G[v]:            # 자식이 없는 leaf node면
        node_cnt_list[v] = 1    # 1을 저장하고
        return 1            # 1 반환

    cnt = 1                 # 아직 세지 않았지만 자식이 있으면 본인 노드 +1
    for node in G[v]:       # 자식을 순회
        cnt += count_node(node)  # 자식 노드의 숫자 누적

    node_cnt_list[v] = cnt  # 저장
    return cnt


N, R, Q = map(int, input().split())

G = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())
    G[U].append(V)
    G[V].append(U)

visited = [0 for _ in range(N+1)]
remove_parent(R)    # 부모 노드 제거 처리

subtree_root = []   # 서브트리의 노드를 담을 리스트
for _ in range(Q):
    subtree_root.append(int(input()))

node_cnt_list = [0 for _ in range(N+1)]  # 자신이 루트일 때 노드 개수를 담을 리스트
for r in subtree_root:
    if not node_cnt_list[r]:    # 아직 안담겼으면
        ans = count_node(r)     # 세어 봅니다.
    else:                       # 이미 세어봤으면
        ans = node_cnt_list[r]  # 그냥 추출
    print(ans)
