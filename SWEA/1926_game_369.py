N = int(input())

i = 1
while i <= N:
    cnt = 0

    j = i
    while j > 0:
        rem = j % 10 
        if rem in [3,6,9]:
            cnt += 1
        j //= 10

    # i를 문자열로 바꾸어서 접근
    # for str_j in str(i):
    #     j = int(str_j)

    #     if j == 3 or j == 6 or j == 9:
    #         cnt += 1

    if cnt > 0:
        print('-' * cnt, end = ' ')
    
    else:
        print(i, end = ' ')
    i += 1