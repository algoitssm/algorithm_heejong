# https://www.acmicpc.net/problem/4673


def d(n):
    ans = n
    while n:
        ans += n % 10
        n //= 10
    return ans


# print(d(33))
# print(d(39))
# print(d(75))

num_list = [False] * 10001

num = 1

while num <= 10000:
    if d(num) <= 10000:
        num_list[d(num)] = True
    num += 1

for idx in range(1, 10000):
    if num_list[idx] == False:
        print(idx)
