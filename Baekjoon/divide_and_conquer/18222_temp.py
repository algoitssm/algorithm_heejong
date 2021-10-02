# https://www.acmicpc.net/problem/18222

def recursive(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1

    if n % 2:
        return 1 - recursive(n//2)
    else:
        return recursive(n//2)


k = int(input())
print(recursive(k-1))

# Google
# print(bin(int(input())-1).count('1')%2)
