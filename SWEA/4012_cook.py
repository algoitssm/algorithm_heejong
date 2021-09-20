from itertools import combinations

T = int(input())
tc = 1

while tc <= T:

    N = int(input())

    synergies = []    # 재료별 시너지 저장
    for _ in range(N):
        synergies.append(list(map(int, input().split())))

    num_ingredients = N // 2            # 음식당 재료 개수
    idx_list = [n for n in range(N)]    # 재료 번호

    food_tastes_diff = []   # A와 B의 맛 차이를 저장할 리스트

    for case in combinations(idx_list, num_ingredients):    # 재료 개수만큼 골라
        a_food_taste = b_food_taste = 0                     # A와 B의 맛을 계산

        # 먼저 A
        # 고른 재료 개수 중 2개씩 골라서 시너지를 계산 (순서 고려)
        for a_ing1, a_ing2 in combinations(case, 2):
            a_food_taste += synergies[a_ing1][a_ing2]       # i와 j
            a_food_taste += synergies[a_ing2][a_ing1]       # j와 i

        # 다음 B
        # A에서 고르지 않은 재료를 사용 -> 차집합
        for b_ing1, b_ing2 in combinations(set(idx_list) - set(case), 2):
            b_food_taste += synergies[b_ing1][b_ing2]       # 상동
            b_food_taste += synergies[b_ing2][b_ing1]

        food_tastes_diff.append(
            abs(a_food_taste-b_food_taste))  # A와 B의 맛 차이를 저장

    ans = min(food_tastes_diff)     # 그 중에 가장 작은 값이 정답

    print(f'#{tc} {ans}')
    tc += 1
    # break
