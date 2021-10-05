# https://www.acmicpc.net/problem/2447
from pandas import DataFrame


def stamp(r, c, n):

    if n == 3:
        pass

    step = n//3

    if step == 1:
        # print(char*n)
        return

    for r in range(0, n, step):
        for c in range(0, n, step):
            print(r, c)
            stamp(r, c, step)


N = int(input())

G = [['*' for _ in range(N)] for _ in range(N)]
print(DataFrame(G))
stamp(0, 0, N)
