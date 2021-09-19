# https://www.acmicpc.net/problem/2263
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def post_to_pre_order(post_left, post_right, in_left, in_right):

    # print(post_left, post_right)
    if post_left > post_right or in_left > in_right:
        return

    # print('-------------')
    # print('in: ', in_order)
    # print('post: ', post_order)
    # print('left, right: ', post_left, post_right)
    pivot = post_order[post_right]

    # print('in_order: ', in_order[in_left:in_right+1])
    pivot_idx = in_order.index(pivot)
    offset = pivot_idx - in_left

    # pre_order.append(pivot)
    print(pivot, end=' ')

    # post_to_pre_order(post_left, pivot_idx-1, in_left, pivot_idx-1)
    # post_to_pre_order(pivot_idx, post_right-1, pivot_idx+1, in_right)

    post_to_pre_order(post_left, post_left+offset-1, in_left, pivot_idx-1)
    post_to_pre_order(post_left+offset, post_right-1, pivot_idx+1, in_right)


n = int(input())

pre_order = []
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

# post_left = in_left = 0
# post_right = in_right = n-1
post_to_pre_order(0, n-1, 0, n-1)

# print(*pre_order)

# 8
# 5 6 8 4 3 1 2 7
# 5 8 4 6 2 1 7 3

# 3 6 5 4 8 7 1 2
