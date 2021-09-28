import sys
sys.stdin = open('input.txt')


def check(n, my_sum):
    global min_sum

    if n >= 12:
        if min_sum > my_sum:
            min_sum = my_sum
        return

    check(n + 1, my_sum + min(prices[0]*plans[n+1], prices[1]))

    check(n + 3, my_sum + prices[2])


for tc in range(int(input())):
    prices = list(map(int, input().split()))    # [일, 달, 3달, 년]
    plans = [0] + list(map(int, input().split()))
    # month_pay_check = [0 for _ in range(12)]

    # month_pay = [0 for _ in range(12+1)]

    min_sum = prices[3]
    check(0, 0)     # n, sum

    # total_swimming_days = sum(plans)

    print('#{0} {1}'.format(tc+1, min_sum))
    # break
