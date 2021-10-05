# https://www.acmicpc.net/problem/1074


def Z(r, c, n):
    global cnt, chk

    if chk:
        return

    if n == 1:
        if r == R and c == C:
            chk = 1
            print(cnt)
        cnt += 1
        return

    for row in range(r, r + 1 << n, 2):
        for col in range(c, c + 1 << n, 2):

            step = n >> 1
            Z(row, col, step)
            Z(row, col+step, step)
            Z(row+step, col, step)
            Z(row+step, col+step, step)
            if chk:
                return


N, R, C = map(int, input().split())

cnt = 0
chk = 0
Z(0, 0, N)
