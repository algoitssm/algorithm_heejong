# https://www.acmicpc.net/problem/21758

import sys

N = int(sys.stdin.readline())

spots = tuple(map(int, sys.stdin.readline().split()))

honey_total = sum(spots)    # 꿀의 총 합을 미리 계산

# 2 가지 케이스

# 1) 벌 - 꿀통 - 벌

# 만약 9-9-4-1-4-9-9 로 되어 있다면
# 양 끝 9는 벌이 있고 나머지 spot 중 꿀통이 있다.
# 가장 꿀의 양이 많은 spot에 꿀통이 있어야 양 벌 둘 다 채취가 가능
# 따라서 총 꿀을 다 더하고 양 끝을 빼고 최대값은 한 번 더 더함

# max_spot = spots[0]
# honey_sum1 = 0
# for idx in range(1, N - 1):
#     if max_spot < spots[idx]:
#         max_spot = spots[idx]
#     honey_sum1 += spots[idx]
# honey_sum1 += max_spot

honey_sum1 = honey_total - spots[0] - spots[-1] + max(spots)


# 2) 벌 - 벌 - 꿀통 또는 꿀통 - 벌 -벌

# 어느 곳에 꿀통을 둘 지 어떻게 판별할 것인가?
# 반으로 나누어서 더 꿀이 많은 쪽에 꿀통?

# mid_spot = N // 2

# if not N & 1:   # 짝수면
#     if sum(spots[:mid_spot]) > sum(spots[mid_spot:]):   # 반으로 갈라서 꿀이 왼쪽에 더 많으면
#         spots.reverse()                                 # 역순 정렬
# else:           # 홀수면
#     if sum(spots[:mid_spot]) > sum(spots[mid_spot+1:]):  # 정 중앙의 꿀을 제외하고 비교
#         spots.reverse

# 아니더라...


# 양 옆을 둘 다 구해서 큰 값을 반환 (for문 두 번 쓰기 싫어서)

# _right: 벌-벌-꿀통    _left: 꿀통-벌-벌
# bee_a: 끝에 있는 벌   bee_b: 중간에 있는 벌

honey_spot_right = bee_a_left = N - 1
bee_a_right = honey_spot_left = 0
honey_sum_right = honey_sum_left = 0

# bee_b와 bee_a사이에 있는 꿀을 더할 변수
bee_b_passed_right = spots[0]
bee_b_passed_left = spots[-1]

for bee_b in range(1, honey_spot_right):    # 1부터 N-1까지 순회
    # _right
    bee_b_passed_right += spots[bee_b]      # bee_b가 지나가면서 누적

    # 두 벌이 딴 꿀 = bee_a가 딴 꿀 + bee_b가 딴 꿀
    #              = (총 꿀 - bee_a 위치) + (총 꿀 - (bee_b가 지나친 꿀 + bee_b 위치))
    #              = 2 * 총 꿀 - bee_a 위치 - bee_b 위치 - bee_b가 지나친 꿀
    bee_total_honey_right = 2 * honey_total - \
        spots[0] - spots[bee_b] - bee_b_passed_right

    # _left
    # bee_a_honey_left = sum(spots[:-1]) - spots[bee_b]
    # bee_b_honey_left = sum(spots[:bee_b])
    # bee_total_honey_left = bee_a_honey_left + bee_b_honey_left
    bee_b_passed_left += spots[- 1 - bee_b]
    bee_total_honey_left = 2 * honey_total - \
        spots[-1] - spots[-1-bee_b] - bee_b_passed_left

    # 그 중 bee_b가 어디있을 때 큰 지 구함 (max)
    if honey_sum_right < bee_total_honey_right:
        honey_sum_right = bee_total_honey_right

    if honey_sum_left < bee_total_honey_left:
        honey_sum_left = bee_total_honey_left

# 꿀통-벌-벌 vs 벌-벌-꿀통
if honey_sum_right > honey_sum_left:
    honey_sum2 = honey_sum_right
else:
    honey_sum2 = honey_sum_left

# honey_sum2 = max(honey_sum_right, honey_sum_left)


# 3) 꿀통 - 벌 - 벌
# spots.reverse()

# honey_spot = len(spots) - 1
# bee_a = 0
# honey_sum3 = 0

# for bee_b in range(1, honey_spot):
#     bee_a_honey = sum(spots[1:]) - spots[bee_b]
#     bee_b_honey = sum(spots[bee_b + 1:])
#     bee_total_honey = bee_a_honey + bee_b_honey

#     if honey_sum3 < bee_total_honey:
#         honey_sum3 = bee_total_honey

print(max(honey_sum1, honey_sum2))
