from copy import deepcopy
from itertools import combinations


def check_col(row):
    # print(row)
    chk = row[0]
    cnt = 1

    for i in range(1, len(row)):
        # print(K)
        # print(i, end=' ')
        if row[i] == chk:
            cnt += 1
        else:
            chk = row[i]
            cnt = 1

        if cnt == K:
            return 1

    return 0


def check_all(matrix):
    # print(list(zip(*matrix)))
    result = 1
    for row in zip(*matrix):
        # print(row)
        if result == 0:
            return False
        result *= check_col(row)
    return True


def find_binary_subsets(n):
    ans_list = []
    for i in range(1 << n):
        # i = 1 << ans
        tmp = [0 for _ in range(n)]
        # print(tmp)
        binary_string = bin(i)
        length = len(binary_string)
        # print(binary_string)
        for j in range(1, length):
            if binary_string[-j] == 'b':
                break
            elif binary_string[-j] == '1':
                tmp[-j] = 1
            elif binary_string[-j] == '0':
                continue
        ans_list.append(tmp)

    return ans_list


# def function_test(num):

#     for case in combinations(row_list, num):

#         for subset_case in subset_cases:

#             for idx, row in enumerate(case):

#                 for col in range(W):

#                     films[row][col] = subset_case[idx]

#             if check_all(films):
#                 return
#     # print(ans)


for tc in range(int(input())):
    D, W, K = map(int, input().split())
    films = []

    for _ in range(D):
        films.append(list(map(int, input().split())))

    # print(list(zip(*films)))
    row_list = [n for n in range(D)]
    ans = 0

    t_ans = 0

    # print(check_all(films))

    if not check_all(films):

        while not ans:

            t_ans += 1
            subset_cases = find_binary_subsets(t_ans)

            # print(subset_cases)
            # break

            # function_test(ans)

            for case in combinations(row_list, t_ans):

                if ans:
                    break

                for subset_case in subset_cases:
                    t_films = deepcopy(films)

                    for idx, row in enumerate(case):

                        for col in range(W):

                            t_films[row][col] = subset_case[idx]

                    if check_all(t_films):
                        # print(case)
                        # print(subset_case)
                        ans = t_ans
                        break
            # print(ans)
            # break

    # print(ans)
    print('#{0} {1}'.format(tc+1, ans))
    # break
