T = int(input())

i = 1
while i <= T:
    N, M = map(int, input().split())
    list_N = []

    j = 0
    while j < N:
        list_N.append(list(map(int, input().split())))
        j += 1
    
    cnt = N - M + 1

    
    my_sum = 0
    
    for row in range(cnt):      # 행
                
        for col in range(cnt):  # 열
            tmp_sum = 0

            for r_cnt in range(row, row+M):

                for c_cnt in range(col, col+M):

                    tmp_sum += list_N[r_cnt][c_cnt]
            

            
            if my_sum < tmp_sum:
                my_sum = tmp_sum
        
    print(f'#{i} {my_sum}')

    i += 1
