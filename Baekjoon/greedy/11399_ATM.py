n = int(input())

withdraw_times = list(map(int, input().split()))

withdraw_times.sort()

ans = 0

for idx, time in enumerate(withdraw_times):
    ans += time * (n - idx)

print(ans)
