import sys
sys.stdin = open('input12.txt')


def distance(v, w):
    return abs(v[0] - w[0]) + abs(v[1] - w[1])


def time_to_take(lst: list, length: int):
    lst.sort()

    t_sum = 0
    for idx in range((len(lst)-1) % 3, len(lst)-1, 3):      # 하위 로직을 일반화
        t_sum += lst[idx] + length
    return max(t_sum, lst[-1]) + length + 1

    # if len(lst) <= 3:
    #     return lst[-1] + length + 1

    # elif len(lst) == 4:
    #     return max(lst[0] + length, lst[-1]) + length + 1

    # elif len(lst) == 5:
    #     return max(lst[1] + length, lst[-1]) + length + 1

    # elif len(lst) == 6:
    #     return max(lst[2] + length, lst[-1]) + length + 1

    # elif len(lst) == 7:
    #     return max(lst[0] + length + lst[3] + length, lst[-1]) + length + 1

    # elif len(lst) == 8:
    #     return max(lst[1] + length + lst[4] + length, lst[-1]) + length + 1

    # elif len(lst) == 9:
    #     return max(lst[2] + length + lst[5] + length, lst[-1]) + length + 1


for tc in range(int(input())):

    N = int(input())

    G = [list(map(int, input().split())) for _ in range(N)]

    stairs = []
    persons = []
    for row in range(N):
        for col in range(N):
            if G[row][col] == 1:            # 사람
                persons.append((row, col))
            elif G[row][col] >= 2:          # 계단
                stairs.append((row, col))

    ans = 987654321
    for binaried in range(1 << len(persons)):           # 경우의 수 = 2^(사람수)
        case = bin(binaried)[2:].zfill(len(persons))    # 이진형태로 표현하고 시작

        # [0번째 stair, 1번째 stair]   ex) [[4,2], [4,3,3,2]]
        distance_list = [[], []]
        for idx in range(len(persons)):
            case_idx = int(case[idx])
            distance_list[case_idx].append(
                distance(persons[idx], stairs[case_idx]))   # 걸리는 시간별로 리스트화되어 저장

        times = [0, 0]          # 걸리는 시간 저장 [0번째 계단, 1번째 계단]
        for idx2 in range(2):
            if distance_list[idx2] != []:
                stair_time = G[stairs[idx2][0]][stairs[idx2][1]]    # 계단 시간
                times[idx2] = time_to_take(
                    distance_list[idx2], stair_time)  # 계단당 걸리는 시간을 times에 저장

        if ans > max(times):    # 각 계단의 시간 중 가장 오래 걸리는 시간
            ans = max(times)    # 최소인 경우 갱신

    print('#{} {}'.format(tc+1, ans))
    # break
