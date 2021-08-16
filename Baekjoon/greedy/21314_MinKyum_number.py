# https://www.acmicpc.net/problem/21314

# Unsolved

import sys

input_str = sys.stdin.readline()

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


def max_minkyum(string: str):

    cnt = 0
    output_str = ''

    for val in string:
        if val == 'M':
            cnt += 1
        else:
            output_str += str(5 * int(10 ** cnt))
            cnt = 0
    else:
        if val == 'M':
            output_str += str(1 * int(10 ** (cnt-1)))

    return int(output_str)


def min_minkyum(string: str):

    string = string.replace('K', '5')
    # string = string.replace('M', '1')

    for idx in range(1, len(string)):
        if string[idx] == 'M' and (string[idx-1] == 'M' or string[idx-1] == '0'):
            string = string[:idx] + '0' + string[idx+1:]

    string = string.replace('M', '1')

    return int(string)


# print(max_minkyum('M'))
# print(min_minkyum('M'))
# print(max_minkyum('K'))
# print(min_minkyum('K'))
# print(max_minkyum('MK'))
# print(min_minkyum('MK'))
# print(max_minkyum('KM'))
# print(min_minkyum('KM'))
# print(max_minkyum('MKM'))       # 501
# print(min_minkyum('MKM'))       # 151
# print(max_minkyum('MKKMMK'))    # 505500
# print(min_minkyum('MKKMMK'))    # 155105
# print(max_minkyum('MMKMMMMM'))  # 5001000
# print(min_minkyum('MMKMMMMM'))  # 1051000
# print(max_minkyum('MMMMKKK'))   # 5000055
# print(min_minkyum('MMMMKKK'))   # 1000555

print(max_minkyum(input_str))
print(min_minkyum(input_str))
