# https://www.acmicpc.net/problem/2447


def stamp(r, c, n):

    if n == 1:
        return

    step = n//3

    cnt = 1
    for row in range(r, r+n, step):
        for col in range(c, c+n, step):
            stamp(row, col, step)
            if cnt == 5:
                # print('r,c:, ', row, col)
                for inner_row in range(row, row+step):
                    for inner_col in range(col, col+step):
                        G[inner_row][inner_col] = ' '
            cnt += 1


N = int(input())

G = [['*' for _ in range(N)] for _ in range(N)]
# print(DataFrame(G))

stamp(0, 0, N)

for i in range(len(G)):
    print(''.join(G[i]))
