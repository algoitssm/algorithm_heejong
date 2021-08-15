# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())

i = 0
coins = []
while i < N:
    coins.append(int(input()))
    i += 1

cnt = 0

for coin in coins[::-1]:
    cnt += (K // coin)
    K %= coin

print(cnt)