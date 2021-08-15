# https://www.acmicpc.net/problem/20115

N = int(input())

drinks = list(map(int, input().split()))
drinks.sort(reverse=True)


def mix_drinks(a, b):
    ans1 = a + b/2
    ans2 = b + a/2
    return max(ans1, ans2)


for idx in range(1, N):
    drinks[idx] = mix_drinks(drinks[idx-1], drinks[idx])

print(drinks[-1])
