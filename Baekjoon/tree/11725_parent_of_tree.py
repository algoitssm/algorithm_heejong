# https://www.acmicpc.net/problem/11725

# 그래프 탐색 풀이말고 트리 구조로 풀어 보았습니다.

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def find_parent(n):             # 부모를 찾는 함수
    for branch in tree[n]:      # 해당 노드의 자식에서

        tree[branch].remove(n)  # 그 노드의 자식노드에서 지금 노드를 지우고
        if tree[branch]:        # 남아있다면 (== leaf 노드가 아니라면)
            find_parent(branch)  # 계속 순회
        tree[branch].append(n)  # 마지막에 부모를 붙임


N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    n, m = map(int, input().split())
    tree[n].append(m)
    tree[m].append(n)

find_parent(1)  # 1 (= root 노드)에서 시작

for i in range(2, N+1):  # 1을 제외하고 2부터 순회
    print(tree[i][-1])  # 각 노드 마지막에 부모를 붙였으므로 출력
