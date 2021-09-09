# https://www.acmicpc.net/problem/3584
import sys
sys.setrecursionlimit(100000)


def child_track(n1, n2):
    global chk

    if n1 == n2:
        chk = 1
        return

    for child in childs[n1]:
        child_track(child, n2)


T = int(input())

while T > 0:
    N = int(input())
    childs = [[] for _ in range(N+1)]
    parent = [[] for _ in range(N+1)]
    for _ in range(N-1):
        p, c = map(int, input().split())
        childs[p].append(c)
        parent[c].append(p)

    n1, n2 = map(int, input().split())

    while True:     # 트리라서 공통 부모는 무조건 존재
        chk = 0
        child_track(n1, n2)

        if chk:
            ans = n1
            break

        n1 = parent[n1][0]

    print(ans)
    T -= 1
