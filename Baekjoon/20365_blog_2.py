# https://www.acmicpc.net/problem/20365

N = int(input())

color_list = list(input())


# Recursive TimeError


def change_color(lst, cnt=1):
    start = 0
    end = len(lst)

    chk = 0     # 최초 변경인지 확인을 위한 변수
    for idx in range(1, len(lst)):
        if lst[idx-1] != lst[idx]:
            if chk == 0:
                start = idx     # 최초 변경 때만 바꿈
                chk += 1
            end = idx           # 계속해서 바꿈

    if start == 0 and end == len(lst):  # 변경사항이 없으면
        return cnt
    else:
        return change_color(lst[start:end], cnt+1)


print(change_color(color_list))


# 2중 반복문 시간초과

# start = 0
# end = N
# cnt = 0

# while color_list:
#     # print(color_list)
#     chk = 0
#     cnt += 1

#     for idx in range(1, len(color_list)):
#         if color_list[idx-1] != color_list[idx]:
#             if chk == 0:
#                 start = idx     # 최초 변경 때만 바꿈
#                 chk += 1
#             end = idx           # 계속해서 바꿈

#     if start == 0 and end == len(color_list):   # 한 종류 값만 들어오면
#         break

#     else:
#         color_list = color_list[start:end]

# start = 0
# end = N
# cnt = 0

# for e in color_list:


# print(cnt)
