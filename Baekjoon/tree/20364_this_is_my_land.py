# https://www.acmicpc.net/problem/20364
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

x_list = []
for _ in range(Q):
    x_list.append(int(input()))

# print('----')
blocked = [0 for _ in range(N+1)]

for x in x_list:
    ans = 0
    destination = x
    visited = 0
    # print(x)

    while x > 1:
        if blocked[x]:
            visited = x
        x //= 2

    if visited:
        print(visited)

    else:
        blocked[destination] = 1
        print(0)
