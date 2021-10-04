import sys
from pandas import DataFrame
from copy import deepcopy
sys.stdin = open('input10.txt')


# 포기....

def drop_point(depth):
    global ans
    global G

    if depth == N:
        # print('---------------------')

        # 누적 cnt 횟수 비교
        cnt = 0
        for row in range(H):
            for col in range(W):
                if G[row][col] > 0:
                    cnt += 1

        if ans > cnt:
            print(DataFrame(G))
            print(cnt)
            ans = cnt
        return

    for c in range(W):
        temp = deepcopy(G)
        drop_ball(c)
        drop_point(depth+1)
        G = temp


def drop_ball(c):       # 공 낙하

    # print('start: ', c)
    for r in range(H):
        if G[r][c] != 0:
            brick_break((r, c))

    # 벽돌 터지면 빈공간 채우도록 확인
    refresh(G)


def brick_break(v):     # 벽돌이 터지는 연쇄반응
    # print(v[0], v[1])

    val = G[v[0]][v[1]]

    if val == 0:
        return

    else:
        G[v[0]][v[1]] = 0

        for pos in range(max(0, v[1]-(val-1)), min(W, v[1]+val)):    # 행 연쇄
            # for pos in range(-(val-1), val+1):    # 행 연쇄
            # print(v[0], pos)
            brick_break((v[0], pos))
        for down in range(max(0, v[0]-(val-1)), min(H, v[0]+val)):   # 열 연쇄
            brick_break((down, v[1]))


def refresh(G):      # 공중에 있는 벽돌을 내리는 함수

    for col in range(W):
        zero_idx = H - 1
        while zero_idx >= 0:
            while G[zero_idx][col] != 0:
                zero_idx -= 1
                if zero_idx < 0:
                    break
            if zero_idx < 0:
                break
            for i in range(zero_idx - 1, -1, -1):
                if G[i][col] != 0:
                    break
            else:
                break
            G[i][col], G[zero_idx][col] = G[zero_idx][col], G[i][col]


for tc in range(int(input())):
    N, W, H = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(H)]

    ans = W * H
    drop_point(0)    # 시작 열, 깊이

    print('#{} {}'.format(tc+1, ans))
    break
