import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    prices = list(map(int, input().split()))    # [일, 달, 3달, 년]
    plans = list(map(int, input().split()))
    # month_pay_check = [0 for _ in range(12)]

    month_pay = [0 for _ in range(12)]

    days = months = 0
    mark = -1
    # month_in_row = 0
    for idx, plan in enumerate(plans):
        if idx == mark:
            if sum(month_pay[idx-2:idx+1]) > prices[2]:
                month_pay[idx-2] = 0
                month_pay[idx-1] = 0
                month_pay[idx] = prices[2]
            mark = -1
            pass

        if plan:
            if plan >= prices[1]//prices[0]:
                month_pay[idx] = prices[1]
                # month_pay_check[idx] = 1
                mark = idx+2
                if mark > 12:
                    mark = 11

                # month_in_row += 1

            else:
                month_pay[idx] = plan * prices[0]

    print(month_pay)
    ans = sum(month_pay)
    if ans > prices[3]:
        ans = prices[3]

    # total_swimming_days = sum(plans)

    print('#{0} {1}'.format(tc+1, ans))
    # break
