# import sys
# sys.stdin = open('input3.txt')


def check_col(col):     # 한 줄 성능검사

    chk = col[0]    # 첫 번째 값으로 chk
    cnt = 1

    if cnt == K:    # 성능검사 통과값인 K가 1일 경우 가지치기
        return True  # 참 반환

    for i in range(1, D):

        if col[i] == chk:   # chk랑 같은 값이면
            cnt += 1        # cnt += 1

        else:               # chk랑 다른 값이면
            chk = col[i]    # chk를 바꾸고
            cnt = 1         # 다시 1부터 세자

        # if col[i-1] != col[i]:
        #     cnt = 1
        # else:
        #     cnt += 1

        if cnt == K:        # K까지 세면
            return True     # 참 반환

    return False            # K까지 못 세면 거짓 반환


def check_all(matrix):      # 필름 전체 검사

    result = True           # 값 초기화

    for col in zip(*matrix):    # 한 열 씩 검사해보자

        result = check_col(col)  # 한 열 씩 검사

        if not result:          # 거짓이 하나라도 나오면
            return False        # 필름 전체도 통과 x

    return True             # 다 통과하면 True 반환


def inject(start_row: int, n: int):
    global ans

    if ans:
        return

    if n == t_ans:
        if check_all(films):
            ans = t_ans
        return

    for i in range(start_row, D):
        tmp = []

        for j in range(W):
            tmp.append(films[i][j])
            films[i][j] = 0
        inject(i+1, n+1)

        for j in range(W):
            films[i][j] = 1
        inject(i+1, n+1)

        for j in range(W):
            films[i][j] = tmp[j]


for tc in range(int(input())):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]

    ans = t_ans = 0

    if not check_all(films):

        while not ans:
            t_ans += 1
            inject(0, 0)

    print('#{0} {1}'.format(tc+1, ans))
    # break
