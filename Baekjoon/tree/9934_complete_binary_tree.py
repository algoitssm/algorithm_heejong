# https://www.acmicpc.net/problem/9934
import math


def put_center_num(lst: list, i: int):
    center_idx = len(lst)//2

    ans_list[i].append(lst[center_idx])

    if center_idx == 0:
        return

    put_center_num(lst[:center_idx], i+1)
    put_center_num(lst[center_idx+1:], i+1)


K = int(input())
visit_list = list(map(int, input().split()))

N = len(visit_list)

level = int(math.log2(N + 1))

ans_list = [[] for _ in range(level)]

cnt = 0
put_center_num(visit_list, cnt)

for j in range(level):
    print(*ans_list[j])
