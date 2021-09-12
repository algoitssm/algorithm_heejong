# https://www.acmicpc.net/problem/15681

N, R, Q = map(int, input().split())

G = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())
    G[U].append(V)
    G[V].append(U)

for _ in range(Q):
    pass
