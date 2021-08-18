# https://www.acmicpc.net/problem/21314

import sys

input_str = sys.stdin.readline().rstrip()

# Recursion Error
# def max_minkyum(string: str):

#     if string == 'M':
#         return '1'

#     if string[-1] == 'K' and string.count('K') == 1:
#         return str(5 * (10 ** (len(string)-1)))

#     else:
#         k_idx = string.find('K')
#         # print(string[:k_idx + 1], string[k_idx + 1:])
#         return max_minkyum(string[:k_idx + 1]) + max_minkyum(string[k_idx + 1:])

# 최대가 될 때는 K까지 자름
# 잘랐을 때 자리수를 계산해서


def max_minkyum(string: str):

    cnt = 0
    output_str = ''

    for val in string:
        if val == 'M':  # M일 때마다 카운트
            cnt += 1
        else:           # K가 나오면
            # 누적한 M의 개수 + K 만큼 500... 을 만듦
            output_str += str(5 * int(10 ** cnt))
            cnt = 0                                 # 누적한 M 초기화
    else:                                               # 다 돌았으면
        # M으로 끝나면 (마무리가 K이면 위에서 계산됨)
        if string[-1] == 'M':
            # 누적한 M의 수 만큼 1111.... 을 만듦
            output_str += '1' * cnt

    return int(output_str)  # 숫자로 변환해서 출력


# 최소가 될 때는 K를 5로 바꾸고
# M => 1, MM => 10, MMM => 100 이렇게 바꿈
def min_minkyum(string: str):

    string = string.replace('K', '5')   # K는 5로 바꿈

    for idx in range(1, len(string)):
        # M이고 그 전 문자가 M이거나 0이면
        if string[idx] == 'M' and (string[idx-1] == 'M' or string[idx-1] == '0'):
            string = string[:idx] + '0' + string[idx + 1:]       # M을 0으로 바꿈

    string = string.replace('M', '1')   # 나머지 M을 1로 바꿈

    return int(string)


print(max_minkyum(input_str))
print(min_minkyum(input_str))
