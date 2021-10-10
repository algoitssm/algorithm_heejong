import sys
sys.stdin = open('input13.txt')


for tc in range(int(input())):

    # 접수창구, 정비창구, 고객수, 접수 창구번호, 정비 창구번호
    N, M, K, A, B = map(int, input().split())

    # 접수 창구 = A, 정비 창구 = B
    a_list = list(map(int, input().split()))        # A 창구별 걸리는 시간
    b_list = list(map(int, input().split()))        # B 창구별 걸리는 시간
    t_list = list(map(int, input().split()))        # 손님 도착 시간 (정렬된 형태로 주어지는듯?)

    customer_visit = [[0, 0] for _ in range(K)]     # 고객 K명의 이용한 창구 번호 저장

    a_boxes = [[] for _ in range(len(a_list))]      # A 창구별 소요시간
    a_waiting_queue = []                            # A 창구 대기열

    b_boxes = [[] for _ in range(len(b_list))]      # B 창구별 소요시간
    b_waiting_queue = []                            # B 창구 대기열

    finished = [0 for _ in range(K)]            # 손님이 정비까지 끝냈는지 확인 (반복문 종료)

    time = 0
    while True:
        if all(finished):                           # 모두 정비를 끝 마쳤으면 종료
            break

        for person_idx, t in enumerate(t_list):     # t_list를 순회하면서
            if t == time:                           # 해당시간의 사람을
                a_waiting_queue.append(person_idx)  # A 창구 대기열에 추가

        # A
        for idx in range(len(a_boxes)):             # 접수 창구를 확인

            if a_boxes[idx] != []:                  # 창구에 사람이 있을 때
                if a_boxes[idx][1] > 0:             # 아직 시간이 남았으면
                    a_boxes[idx][1] -= 1            # 하나씩 빼줌

                if a_boxes[idx][1] == 0:            # 시간이 다 되었으면
                    person_idx = a_boxes[idx][0]    # 몇번째 사람인지 보고
                    a_boxes[idx] = []               # 그 창구를 비우고
                    b_waiting_queue.append(person_idx)  # B 창구 대기열에 그 사람 추가

            if a_boxes[idx] == []:                          # 창구가 비었으면
                if a_waiting_queue:                         # A 대기열에 사람이 있으면
                    person_idx = a_waiting_queue.pop(0)     # 제일 처음 온 사람을
                    a_boxes[idx] = [person_idx, a_list[idx]]    # 그 창구에 투입
                    customer_visit[person_idx][0] = idx     # 해당 손님 A 창구번호 저장

        # B
        for idx in range(len(b_boxes)):             # 정비 창구 확인

            if b_boxes[idx] != []:                  # 창구에 사람이 있을 때
                if b_boxes[idx][1] > 0:             # 아직 시간이 남아있으면
                    b_boxes[idx][1] -= 1            # 하나씩 빼줌

                if b_boxes[idx][1] == 0:            # 시간이 다 되었으면
                    person_idx = b_boxes[idx][0]    # 몇번째 사람인지 보고
                    b_boxes[idx] = []               # 그 창구를 비우고
                    finished[person_idx] = 1        # 그 사람 완료 처리

            if b_boxes[idx] == []:                  # 창구가 비었으면
                if b_waiting_queue:                 # B 대기열에 사람이 있으면
                    person_idx = b_waiting_queue.pop(0)         # 제일 처음 온 사람을
                    b_boxes[idx] = [person_idx, b_list[idx]]    # 그 창구에 투입
                    customer_visit[person_idx][1] = idx     # 해당 손님 B 창구번호 저장

        time += 1

    ans = 0
    for idx in range(K):        # 손님 전체 순회
        if customer_visit[idx] == [A-1, B-1]:   # 방문 창구번호가 같으면
            ans += idx + 1      # 그 손님 번호를 누적

    if ans == 0:                # 아무도 없으면
        ans = -1                # -1 출력

    print('#{} {}'.format(tc+1, ans))
    # break
