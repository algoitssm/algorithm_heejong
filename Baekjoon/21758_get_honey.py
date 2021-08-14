# https://www.acmicpc.net/problem/21758

# 55점

N = int(input())

spots = list(map(int, input().split()))

# 2 가지 케이스를 생각

# 1) 벌 - 꿀통 - 벌
honey_sum1 = sum(spots[1:-1]) + max(spots)


# 2) 벌 - 벌 - 꿀통
# mid_spot = N // 2

# if not N & 1:   # 짝수면
#     if sum(spots[:mid_spot]) > sum(spots[mid_spot:]):   # 반으로 갈라서 꿀이 왼쪽에 더 많으면
#         spots.reverse()                                 # 역순 정렬
# else:           # 홀수면
#     if sum(spots[:mid_spot]) > sum(spots[mid_spot+1:]):  # 정 중앙의 꿀을 제외하고 비교
#         spots.reverse

honey_spot_left = bee_a_right = len(spots) - 1
bee_a_left = honey_spot_right = 0
honey_sum_left = honey_sum_right = 0

for bee_b in range(1, honey_spot_left):
    bee_a_honey_left = sum(spots[1:]) - spots[bee_b]
    bee_b_honey_left = sum(spots[bee_b + 1:])
    bee_total_honey_left = bee_a_honey_left + bee_b_honey_left

    bee_a_honey_right = sum(spots[:-1]) - spots[bee_b]
    bee_b_honey_right = sum(spots[:bee_b])
    bee_total_honey_right = bee_a_honey_right + bee_b_honey_right

    if honey_sum_left < bee_total_honey_left:
        honey_sum_left = bee_total_honey_left

    if honey_sum_right < bee_total_honey_right:
        honey_sum_right = bee_total_honey_right

if honey_sum_left > honey_sum_right:
    honey_sum2 = honey_sum_left
else:
    honey_sum2 = honey_sum_right

# honey_sum2 = max(honey_sum_left, honey_sum_right)


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


# print(spots)
# print(honey_spot, bee_a)
