# https://www.acmicpc.net/problem/16953

A, B = map(int, input().split())

# print(A, B)

cnt = 1
while True:

    if B == A:
        break

    if not B % 2 and B > A:
        # print(B)
        B //= 2
    else:
        if B % 10 == 1:
            B //= 10

        else:
            cnt = -1
            break

    cnt += 1

print(cnt)
