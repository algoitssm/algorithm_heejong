# https://www.acmicpc.net/problem/1343

board_panel = list(input())

pol_a = ['A', 'A', 'A', 'A']
pol_b = ['B', 'B']

cnt = 0
for idx in range(len(board_panel)):

    if board_panel[idx] == 'X':
        cnt += 1

    else:
        if cnt & 1:
            print(-1)
            break
        else:

            # 생각대로 코드 구현
            # if not cnt % 4:
            #     while cnt > 0:
            #         board_panel[idx-cnt] = 'A'
            #         cnt -= 1
            # else:
            #     while cnt > 2:
            #         board_panel[idx-cnt] = 'A'
            #         cnt -= 1
            #     board_panel[idx-2] = 'B'
            #     board_panel[idx-1] = 'B'

            # 위를 더 간편하게
            remain = cnt % 4
            while cnt > remain:
                board_panel[idx-cnt] = 'A'
                cnt -= 1
            
            if cnt % 4:
                board_panel[idx-2] = 'B'
                board_panel[idx-1] = 'B'

            cnt = 0
else:
    if cnt & 1:
        print(-1)
    else:
        idx = len(board_panel)
        remain = cnt % 4
        while cnt > remain:
            board_panel[idx-cnt] = 'A'
            cnt -= 1
        
        if cnt % 4:
            board_panel[idx-2] = 'B'
            board_panel[idx-1] = 'B'

        print(''.join(board_panel))