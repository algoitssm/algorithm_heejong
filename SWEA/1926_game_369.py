N = int(input())

i = 1
while i <= N:
    cnt = 0

    for str_j in str(i):
        j = int(str_j)

        if j == 3 or j == 6 or j == 9:
            cnt += 1

    if cnt > 0:
        print('-' * cnt, end = ' ')
    
    else:
        print(i, end = ' ')
    i += 1