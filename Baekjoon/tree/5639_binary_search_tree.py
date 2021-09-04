# https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit(100000)


def pre_to_post_order(lst: list):

    if not lst:
        return

    pivot = lst[0]

    for idx in range(1, len(lst)):
        if lst[idx] > pivot:
            pre_to_post_order(lst[1:idx])
            pre_to_post_order(lst[idx:])
            ans.append(pivot)
            return

    pre_to_post_order(lst[1:])
    ans.append(pivot)


nums = []
while True:
    try:
        num = input()
        nums.append(int(num))
    except:
        break

ans = []
pre_to_post_order(nums)
print(*ans, sep='\n')
