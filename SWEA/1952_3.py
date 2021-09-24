import sys
sys.stdin = open('input.txt')


# def calc(cost, m):  # (이전 달까지의 계산 결과, 현재 내가 보낼 결과)
#     global min_cost

#     if m > 12:
#         if min_cost > cost:
#             min_cost = cost
#         return

#     # # 1일권
#     # calc(cost + d * month[m], m + 1)
#     # # 1달권
#     # calc(cost + m1, m + 1)
#     calc(cost + min(d*month[m], m1), m+1)

#     # 3달권
#     calc(cost + m3, m + 3)


for tc in range(int(input())):
    d, m1, m3, y = map(int, input().split())    # [일, 달, 3달, 년]
    month = [0] + list(map(int, input().split()))
    # month_pay_check = [0 for _ in range(12)]

    dp = [0] * 13   # 해당 월까지의 최소값이 저장되어있음
    dp[1] = min(m1, month[1]*d)
    dp[2] = dp[1] + min(m1, month[2]*d)

    for i in range(3, 13):
        dp[i] = min(dp[i-3] + m3, dp[i-1] + m1, dp[i-1] + month[i] * d)

    print('#{0} {1}'.format(tc+1, min(dp[12], y)))
    # break
