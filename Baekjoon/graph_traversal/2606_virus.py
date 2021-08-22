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


# 1. 첫 번째 풀이

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

# 두 번재 풀이: 37%에서 멈춤.... => 1에서 갈라질 때를 생각
# ***stack.pop() 을 계속 돌면 안됨**** => 가장 처음 pop된 것을 어떻게 처리할 것인가

# v = 1
# stack = [v]  # 1에서 시작
# while v > 0:        # while stack: 에서 바꿈
#     visited[v] = 1
#     for w in range(N+1):
#         if adj[v][w] == 1 and not visited[w]:
#             stack.append(w)         # 얘를 v로 바꾸면 통과가 됨
#             # visited[w] = 1
#             v = w
#             break
#     else:
#         if stack:
#             v = stack.pop()
#         else:
#             v = 0

# 결국 첫 번째 풀이와 비슷하게 나옴


# print(visited)
print(sum(visited)-1)   # 1번 컴퓨터는 뺌
# print(cnt-1)      # cnt를 쓰는 방법?
