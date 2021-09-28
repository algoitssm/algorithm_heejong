import sys
sys.stdin = open('input.txt')


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
