# https://www.acmicpc.net/problem/2630


def divide_and_conquer(r, c, length):

    initial_val = papers[r][c]

    for row in range(r, r+length):
        for col in range(c, c+length):
            if papers[row][col] != initial_val:
                divide_and_conquer(r, c, length//2)
                divide_and_conquer(r+length//2, c, length//2)
                divide_and_conquer(r, c+length//2, length//2)
                divide_and_conquer(r+length//2, c+length//2, length//2)
                return

    cnts[initial_val] += 1


N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

cnts = [0, 0]   # 0 색종이, 1 색종이

divide_and_conquer(0, 0, N)

print(*cnts, sep='\n')
