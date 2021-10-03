# https://www.acmicpc.net/problem/1992


def quad_tree(r, c, n):

    initial_val = G[r][c]

    for row in range(r, r+n):
        for col in range(c, c+n):
            if G[row][col] != initial_val:
                print('(', end='')
                quad_tree(r, c, n//2)
                quad_tree(r, c+n//2, n//2)
                quad_tree(r+n//2, c, n//2)
                quad_tree(r+n//2, c+n//2, n//2)
                print(')', end='')
                return

    print(initial_val, end='')


N = int(input())

G = [list(input()) for _ in range(N)]

quad_tree(0, 0, N)
