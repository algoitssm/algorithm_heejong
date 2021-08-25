# https://www.acmicpc.net/problem/2606

N = int(input())
num_NW = int(input())

adj = [[0]*(N+1) for _ in range(N+1)]

for _ in range(num_NW):
    i, j = map(int, input().split())
    adj[i][j] = 1
    adj[j][i] = 1

visited = [0] * (N+1)


# 1. 첫 번째 풀이

stack = []
v = 1   # 1번 컴퓨터를 통해
while v != 0:
    for w in range(1, N+1):
        if adj[v][w] == 1 and visited[w] == 0:
            stack.append(v)
            v = w
            visited[w] = 1
            break
    else:
        if stack:
            v = stack.pop()
        else:
            v = 0

print(sum(visited)-1)
