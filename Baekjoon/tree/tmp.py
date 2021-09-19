def post_to_pre_order(post_list: list, in_list: list):

    if not post_list:
        return

    pivot = post_list[-1]

    pivot_idx = in_list.index(pivot)
    pre_order.append(pivot)
    post_to_pre_order(post_list[:pivot_idx], in_list[:pivot_idx])
    post_to_pre_order(post_list[pivot_idx:-1], in_list[pivot_idx+1:])


n = int(input())

pre_order = []
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
post_to_pre_order(post_order, in_order)

print(*pre_order)
