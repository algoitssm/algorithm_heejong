# https://www.acmicpc.net/problem/1074


def Z(row, col, n):
    global cnt
    # print(row, col, n)

    if n == 1:
        print(cnt)
        return

    n_halved = n >> 1

    if row <= r < row+n_halved and col <= c < col+n_halved:
        Z(row, col, n_halved)
    cnt += n_halved ** 2

    if row <= r < row+n_halved and col+n_halved <= c < col+n:
        Z(row, col+n_halved, n_halved)
    cnt += n_halved ** 2

    if row+n_halved <= r < row+n and col <= c < col+n_halved:
        Z(row+n_halved, col, n_halved)
    cnt += n_halved ** 2

    if row+n_halved <= r < row+n and col+n_halved <= c < col+n:
        Z(row+n_halved, col+n_halved, n_halved)
    cnt += n_halved ** 2


N, r, c = map(int, input().split())

cnt = 0
Z(0, 0, 1 << N)
