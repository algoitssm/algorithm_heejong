# https://www.acmicpc.net/problem/14916

n = int(input())

change_money = [5, 2]

# 그냥 하드코딩해서 구현

# cnt = n // change_money[0]
# n %= change_money[0]
# if n & 1:
#     cnt -= 1
#     n += change_money[0]

# cnt += n // change_money[1]

# print(cnt)


def money_change(n):
    cnt = 0

    # 거스름돈 반환이 될 수 없는 경우
    if n < 5 and n & 1:
        return -1

    for e in change_money:
        cnt += n // e  # cnt에 나눈 몫을 저장
        n %= e

        if n & 1:  # n이 홀수면 (홀수면 두번째 인자인 2로 나눔x)  # n % 2
            cnt -= 1  # cnt -1
            n += e  #

    return cnt


print(money_change(n))
