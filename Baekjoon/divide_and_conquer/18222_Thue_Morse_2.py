# https://www.acmicpc.net/problem/18222
from math import log2

# k = int(input())

# n = int(log2(k))
# x = '0'

# i = 0
# while i <= n:
#     x2 = ''
#     for char in x:
#         x2 += str((int(char) + 1) % 2)
#     x += x2
#     i += 1

# print(x)
# print(x[k-1])

k = int(input())

n = int(log2(k))
x = '0'

i = 0
while i <= n:
    x2 = ''
    for char in x:
        x2 += str((int(char) + 1) % 2)
    x += x2
    i += 1

print(x)
print(x[k-1])
