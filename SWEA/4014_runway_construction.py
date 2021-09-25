import sys
sys.stdin = open('input8.txt')


def construct(adj):
    global ans

    for row in adj:         # 한 줄씩 검사
        chk = True          # False이면 경사로 만들기에 부적합

        cur_height = row[0]  # 현재 높이 = 시작점
        cnt = 1             # 하나씩 카운트

        i = 1               # 인덱스 1부터 시작
        while i < N:        # 범위 안에서 하나씩 탐색

            if row[i] == cur_height:    # 같은 높이면
                cnt += 1                # cnt + 1

            elif row[i] == cur_height + 1:  # 하나 크면
                if cnt < X:                 # 이 때까지 cnt가 X보다 작으면
                    chk = False             # False
                    break
                else:                       # 아니면
                    cur_height = row[i]     # 현재 높이를 바꾸고
                    cnt = 1                 # 다시 cnt 1부터 시작

            elif row[i] == cur_height-1:    # 하나 작으면

                if i+X > N:                 # X를 더해서 범위를 벗어나면
                    chk = False             # False
                    break

                else:                       # 범위 안에 있을 때
                    for h in row[i:i+X]:    # 그 다음 X까지 같은 높이인지 확인
                        if h != row[i]:     # 다른 높이가 있으면
                            chk = False     # False
                            break
                    else:                   # 경사로 충분히 놓을 수 있으면
                        cur_height = row[i]  # 현재 높이를 바꾸고
                        cnt = 0             # cnt 1이 아니라 0부터 시작
                        i += X - 1          # 인덱스 X만큼 건너뜀

            else:                           # 그 외의 경우 (높이가 1이상 차이)
                chk = False                 # False
                break

            i += 1

        if chk:
            # print(row)
            ans += 1    # 정답에 하나씩 추가


for tc in range(int(input())):
    N, X = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(N)]
    # print(G)

    ans = 0

    construct(G)
    construct(zip(*G))

    print('#{0} {1}'.format(tc+1, ans))
    # break
