T = int(input())

i = 1
while i <= T:
    ans = 0
    puzzle = []

    N, K = map(int, input().split())

    # puzzle로 배열을 만듦
    col = 0
    while col < N:
        tmp_list = list(map(int, input().split()))
        puzzle.append(tmp_list)
        col += 1


    # 첫번째 1의 인덱스를 반환해서 열별로, 행별로 계산...
    # 또 1이 마지막 인덱스일 때를 생각하면서 여러가지 경우의 수를 계산하다가
    # 도저히 모르겠어서 산책한번하고 구글에서 힌트를 조금 받아서
    # 2중 반복문을 구현해 보았습니다...
    # 진짜 너무 어려웠음ㅠ

    # 가로를 계산
    for row in range(N):
        cnt = 0

        for col in range(N):
            if puzzle[row][col] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            else:
                cnt += 1

        if cnt == K:
            ans += 1
                    
    # 세로를 계산
    for col in range(N):
        cnt = 0

        for row in range(N):
            if puzzle[row][col] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            else:
                cnt += 1

        if cnt == K:
            ans += 1

    print(f'#{i} {ans}')

    i += 1