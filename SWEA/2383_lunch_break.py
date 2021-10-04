import sys
from collections import deque
sys.stdin = open('input12.txt')


def distance(v, w):
    return abs(v[0] - w[0]) + abs(v[1] - w[1])


# 원래 재귀로 구현했어야 하는데 케이스가 적어서 생각해본 부끄러운 풀이네요..
def time_to_take(lst: list, length: int):
    lst.sort()

    if len(lst) <= 3:
        return lst[-1] + length + 1

    elif len(lst) == 4:
        return max(lst[0] + length, lst[-1]) + length + 1

    elif len(lst) == 5:
        return max(lst[1] + length, lst[-1]) + length + 1

    elif len(lst) == 6:
        return max(lst[2] + length, lst[-1]) + length + 1

    elif len(lst) == 7:
        return max(lst[0] + length + lst[3] + length, lst[-1]) + length + 1

    elif len(lst) == 8:
        return max(lst[1] + length + lst[4] + length, lst[-1]) + length + 1

    elif len(lst) == 9:
        return max(lst[2] + length + lst[5] + length, lst[-1]) + length + 1


for tc in range(int(input())):

    N = int(input())

    G = [list(map(int, input().split())) for _ in range(N)]

    stairs = []
    persons = []
    for row in range(N):
        for col in range(N):
            if G[row][col] == 1:
                persons.append((row, col))
            elif G[row][col] >= 2:
                stairs.append((row, col))

    ans = 987654321
    for binaried in range(1 << len(persons)):
        case = bin(binaried)[2:].zfill(len(persons))

        distance_list = [[], []]
        for idx in range(len(persons)):
            case_idx = int(case[idx])
            distance_list[case_idx].append(
                distance(persons[idx], stairs[case_idx]))

        times = [0, 0]
        for idx2 in range(2):
            if distance_list[idx2] != []:
                stair_time = G[stairs[idx2][0]][stairs[idx2][1]]
                times[idx2] = time_to_take(distance_list[idx2], stair_time)

        if ans > max(times):
            ans = max(times)

    print('#{} {}'.format(tc+1, ans))
    # break
