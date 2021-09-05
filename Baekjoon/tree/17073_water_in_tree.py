# https://www.acmicpc.net/problem/17073
import sys
input = sys.stdin.readline

N, W = map(int, input().split())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

cnt = 0
for idx, edge in enumerate(tree):
    if idx != 1 and len(edge) == 1:
        cnt += 1

print(W/cnt)
