# https://www.acmicpc.net/problem/4256

def to_postfix_reading(pre_list, in_list):

    if not in_list:
        return

    root = pre_list[0]
    idx = in_list.index(root)
    to_postfix_reading(pre_list[1:idx+1], in_list[:idx])
    to_postfix_reading(pre_list[idx+1:], in_list[idx+1:])
    postfix_read.append(root)


T = int(input())

while T > 0:
    n = int(input())

    prefix_read = list(map(int, input().split()))
    infix_read = list(map(int, input().split()))
    postfix_read = []

    to_postfix_reading(prefix_read, infix_read)

    print(*postfix_read)

    T -= 1
