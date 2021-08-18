# https://www.acmicpc.net/problem/2606
# from pandas import DataFrame

N = int(input())
num_NW = int(input())

adj = [[0]*(N+1) for _ in range(N+1)]

for _ in range(num_NW):
    i, j = map(int, input().split())
    adj[i][j] = 1
    adj[j][i] = 1

# print(DataFrame(adj))

visited = [0] * (N+1)
stack = []
i = 1   # 1번 컴퓨터를 통해
while i != 0:
    for w in range(1, N+1):
        # print(w)
        if adj[i][w] == 1 and visited[w] == 0:
            stack.append(i)
            i = w
            visited[w] = 1
            break
    else:
        if stack:
            i = stack.pop()
        else:
            i = 0

# print(visited)
print(sum(visited)-1)  # 1번 컴퓨터는 뺌
