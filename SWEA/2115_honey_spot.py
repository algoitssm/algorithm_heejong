import sys
from itertools import combinations
sys.stdin = open('input7.txt')


def find_max(b: list, max_choices):

    if sum(b) <= C:     # 합이 C 이하면
        return sum([e ** 2 for e in b])  # 그냥 계산

    index_list = [i for i in range(len(b))]

    for i in range(1, len(b)):  # 요소 중 1개, 2개, 3개 ... len(b)+1일 경우는 위에서 처리

        for case in combinations(index_list, i):    # 가능한 인덱스 경우의 수를 뽑자
            # print(case)
            tmp_max = 0     # 요소의 제곱 합을 계산
            b_sum = 0       # 요소의 합을 계산

            for idx in case:
                b_sum += b[idx]
                # print(b[idx], end=' ')
                tmp_max += b[idx] ** 2

            if b_sum <= C:  # 요소의 합이 C이하일 때
                if tmp_max > max_choices:   # 요소 합이 최대로 나오면
                    max_choices = tmp_max   # 갱신

    return max_choices


def choose_spot(base_i, v):
    global max_price

    if v == 2:  # 0 다음 1 다음 2

        price_total = 0     # 이 경우 총 가격을 담을 경우
        # print(honey_box)
        for box in honey_box:   # honey_box에 두 개가 있는데 하나씩 계산
            # print(box)
            max_choices = 0
            price_total += find_max(box, max_choices)

        if price_total > max_price:    # 가장 높은 가격이 나올 경우
            # print(honey_box)
            max_price = price_total    # 가격 갱신

        return

    for i in range(base_i, N):
        for j in range(N-M+1):
            if G[i][j] and G[i][j+M-1]:     # [0, .... , 0] 이면 계산할 필요X
                honey_box[v] = G[i][j:j+M]

                if v != 1:
                    tmp = []
                    for k in range(M):
                        tmp.append(G[i][j+k])
                        G[i][j+k] = 0
                # print(G)
                choose_spot(i+1, v+1)
                if v != 1:
                    for k in range(M):
                        G[i][j+k] = tmp[k]
                honey_box[v].clear()
                # print(G)


for tc in range(int(input())):
    N, M, C = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(N)]
    max_price = 0   # 최대 가격
    honey_box = [[], []]    # 사람1, 사람2

    choose_spot(0, 0)   # 시작 행 번호, 사람 번호 (시작 행 번호 없이하면 조합이 아니라 순열로 나옴)

    print('#{0} {1}'.format(tc+1, max_price))
    # break
