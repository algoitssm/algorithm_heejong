import sys
# from itertools import product
sys.stdin = open('input6.txt')


def dfs(idx, result):
    global max_num, min_num

    idx += 1

    if idx == N:
        # print('final_result: ', result)
        if result > max_num:
            max_num = result
        if result < min_num:
            min_num = result
        # print('min, max: ', min_num, max_num)
        return

    for i in range(4):

        if operators[i] > 0:

            operators[i] -= 1

            if i == 0:  # +이면
                # result += nums[idx]
                # print('result: ', result)
                dfs(idx, result+nums[idx])
            elif i == 1:
                # result -= nums[idx]
                # print('result: ', result)
                dfs(idx, result-nums[idx])
            elif i == 2:
                # result *= nums[idx]
                # print('result: ', result)
                dfs(idx, result*nums[idx])
            elif i == 3:
                # result /= nums[idx]
                # print('result: ', result)
                if nums[idx] == 0:
                    continue
                dfs(idx, int(result/nums[idx]))
            operators[i] += 1


for tc in range(int(input())):
    N = int(input())
    operators = list(map(int, input().split()))   # + - * /
    nums = list(map(int, input().split()))

    max_num = -100000000
    min_num = 100000000

    dfs(0, nums[0])
    # print(max_num, min_num)
    ans = max_num - min_num
    # print(operators)
    # print(list(product(['', '+', '++'], range(3), range(4))))
    # for i in product('+' * operators[0], '-'*operators[1], '*'*operators[2], '/'*operators[3]):
    #     print(i)

    # ans = 0

    print('#{} {}'.format(tc+1, ans))
    # break
