import sys
from copy import deepcopy
from itertools import combinations
sys.stdin = open('input3.txt')

# Time Error


def check_col(row):     # 한 줄 성능검사

    chk = row[0]    # 첫 번째 값으로 chk
    cnt = 1

    if cnt == K:    # 성능검사 통과값인 K가 1일 경우 가지치기
        return True  # 참 반환

    for i in range(1, len(row)):

        if row[i] == chk:   # chk랑 같은 값이면
            cnt += 1        # cnt += 1

        else:               # chk랑 다른 값이면
            chk = row[i]    # chk를 바꾸고
            cnt = 1         # 다시 1부터 세자

        if cnt == K:        # K까지 세면
            return True     # 참 반환

    return False            # K까지 못 세면 거짓 반환


def check_all(matrix):      # 필름 전체 검사

    result = True           # 값 초기화

    for col in zip(*matrix):    # 한 열 씩 검사해보자

        if not result:          # 거짓이 하나라도 나오면
            return False        # 필름 전체도 통과 x

        result = check_col(col)  # 한 열 씩 검사

    return True             # 다 통과하면 True 반환


# # n=1일 때 [0, 1], n=2일 때 [00, 01, 10, 00], .. 을 만들고 싶음
# def find_binary_cases(n):

#     ans_list = []

#     for i in range(1 << n):     # 2의 n승 까지

#         tmp = [0 for _ in range(n)]     # [0], [00], [000], ..  이런식으로 초기화

#         binary_string = bin(i)  # 이진수 변환이라서 '0b0101' 이런 꼴로 나옴

#         for j in range(1, len(binary_string)):  # j를 사용해서 거꾸로 탐색해보자
#             # letter_to_check = binary_string[-j]
#             if binary_string[-j] == 'b':    # b를 만나면
#                 break                       # 그만
#             elif binary_string[-j] == '1':  # 1을 만나면
#                 tmp[-j] = 1                 # 1로 갱신
#             # elif letter_to_check == '0':  # 0일 때는 필요x
#             #     continue
#         ans_list.append(tmp)

#     return ans_list


# n=1일 때 [0, 1], n=2일 때 [00, 01, 10, 00], .. 을 만들고 싶음
def find_binary_cases(n):

    ans_list = []

    for i in range(1 << n):     # 0부터 2의 n승 까지

        tmp = [0 for _ in range(n)]     # [0], [00], [000], ..  이런식으로 초기화

        binary_string = bin(i)  # 이진수 변환이라서 '0b0101' 이런 꼴로 나옴
        # print(binary_string)
        # ans_list.append(list(map(int, str(binary_string[2:]).zfill(n))))
        # print(ans_list)

        # ans_list = []

        for j in range(1, len(binary_string)):  # j를 사용해서 거꾸로 탐색해보자
            # letter_to_check = binary_string[-j]
            if binary_string[-j] == 'b':    # b를 만나면
                break                       # 그만
            elif binary_string[-j] == '1':  # 1을 만나면
                tmp[-j] = 1                 # 1로 갱신
            # elif letter_to_check == '0':  # 0일 때는 필요x
            #     continue
        ans_list.append(tmp)

    # print(ans_list, ans2_list)
    return ans_list


for tc in range(int(input())):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]

    # for _ in range(D):
    #     films.append(list(map(int, input().split())))

    # print(list(zip(*films)))
    row_list = [n for n in range(D)]    # 행 인덱스 리스트
    ans = t_ans = 0     # 약품 주입 횟수

    # print(check_all(films))

    if not check_all(films):    # 성능검사 통과를 못하면

        while not ans:  # 통과할 때 까지 반복 (통과할 때 ans를 갱신할거임)

            t_ans += 1  # 임시 변수 + 1

            # 1일 때 [[0], [1]],  2일 때 [[0,0], [0,1], [1,0], [1,1]], ...
            binary_cases = find_binary_cases(t_ans)
            # print(binary_cases)

            for rows in combinations(row_list, t_ans):  # 행 인덱스 리스트에서 주입할 경우를 뽑자
                # print('rows: ', rows)

                if ans:     # 성능검사 통과했으면
                    break   # 이제 그만

                for binary_case in binary_cases:    # t_ans=2 일 때 => 00, 01, 10, 11, ...
                    # print('binary_case: ', binary_case)
                    # films는 계속 보관해야하므로 deepcopy사용
                    t_films = deepcopy(films)

                    for idx, row in enumerate(rows):

                        for col in range(W):

                            # 전부 0 또는 1로 변경
                            t_films[row][col] = binary_case[idx]
                            # print(binary_case[idx])

                    if check_all(t_films):  # 성능검사 통과하면
                        ans = t_ans         # 최소 횟수 갱신
                        break

    print('#{0} {1}'.format(tc+1, ans))
    # break
