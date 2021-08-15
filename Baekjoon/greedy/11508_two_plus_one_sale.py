# https://www.acmicpc.net/problem/11508

N = int(input())

yogurts = []

for _ in range(N):
    yogurts.append(int(input()))

# print(yogurts)
yogurts.sort(reverse=True)

money_to_pay = 0
for idx, yogurt in enumerate(yogurts):
    if (idx + 1) % 3:       # 3번째로 비싼 유제품은 더하지 않음 = 3으로 나눈 나머지가 있을 때만 더함
        money_to_pay += yogurt

print(money_to_pay)
