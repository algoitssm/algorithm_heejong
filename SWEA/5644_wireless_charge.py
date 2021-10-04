import sys
sys.stdin = open('input11.txt')


def find_ap(v):     # 근처의 충전기를 구하는 함수

    ap_list = []

    for case in v:
        tmp_list = []
        for idx, ap in enumerate(aps):
            if abs(case[0]-(ap[1]-1)) + abs(case[1]-(ap[0]-1)) <= ap[2]:    # 열행 입력 주의
                tmp_list.append(idx)
        ap_list.append(tmp_list)

    return ap_list  # 해당 리스트 반환


def intersection_charge(n, my_sum):      # 겹칠 때 충전 (n=0일 때 A, n=1일 때 B)
    global tmp_sum

    if n == 2:
        if tmp_sum < my_sum:
            tmp_sum = my_sum
        return

    for aps_idx in near_aps[n]:
        tmp = aps[aps_idx][3]
        aps[aps_idx][3] = 0
        intersection_charge(n+1, my_sum + tmp)
        aps[aps_idx][3] = tmp


for tc in range(int(input())):
    M, A = map(int, input().split())
    G = [[0 for _ in range(10)] for _ in range(10)]
    paths = [list(map(int, input().split())) for _ in range(2)]
    aps = [list(map(int, input().split()))
           for _ in range(A)]   # col, row, C, P

    coords = [[0, 0], [9, 9]]   # A좌표, B좌표

    near_aps = find_ap(coords)

    charge_sum = 0  # 총 누적합 => 정답으로 제출

    # 시작 지점에서 먼저 체크
    intersection = set(near_aps[0]).intersection(set(near_aps[1]))    # 겹치는게 있나

    if intersection:
        tmp_sum = 0
        aps_count = [0 for _ in range(A)]
        intersection_charge(0, 0)   # n, sum
        charge_sum += tmp_sum

    else:

        for case in near_aps:
            if case:
                case_charge_max = 0
                for ap_idx in case:
                    if case_charge_max < aps[ap_idx][3]:
                        case_charge_max = aps[ap_idx][3]
                charge_sum += case_charge_max

    # 시작지점 이후
    for i in range(M):    # 시간별 순회

        # 좌표 이동
        for j in range(2):
            if paths[j][i] == 0:    # 0이면 제자리 (이 부분 놓쳐서 한참 걸림)
                continue
            elif paths[j][i] == 1:
                coords[j][0] -= 1
            elif paths[j][i] == 2:
                coords[j][1] += 1
            elif paths[j][i] == 3:
                coords[j][0] += 1
            else:
                coords[j][1] -= 1

        near_aps = find_ap(coords)  # 각각 충전 가능한 AP 선택

        intersection = set(near_aps[0]).intersection(
            set(near_aps[1]))    # 겹치는게 있나

        if intersection:
            tmp_sum = 0
            aps_count = [0 for _ in range(A)]
            intersection_charge(0, 0)   # n, sum 전달
            charge_sum += tmp_sum

        else:
            for case in near_aps:
                if case:
                    case_charge_max = 0
                    for ap_idx in case:
                        if case_charge_max < aps[ap_idx][3]:
                            case_charge_max = aps[ap_idx][3]
                    charge_sum += case_charge_max

    print('#{} {}'.format(tc+1, charge_sum))
    # break
