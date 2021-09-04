# https://www.acmicpc.net/problem/11725
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def find_parent(n):
    for branch in tree[n]:

        tree[branch].remove(n)
        if tree[branch]:
            find_parent(branch)
        tree[branch].append(n)


N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    n, m = map(int, input().split())
    tree[n].append(m)
    tree[m].append(n)

find_parent(1)

for i in range(2, N+1):
    print(tree[i][-1])
