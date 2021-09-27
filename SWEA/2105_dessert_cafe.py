import sys
sys.stdin = open('input9.txt')

# 남서 남동 북동 북서
dr = (1, 1, -1, -1)
dc = (-1, 1, 1, -1)


def cafe_tour(d, v):    # d 방향정보, v 위치
    global ans

    if 3 <= d < 5 and v == start_point:     # d=3이면 원래 방향, d=4이면 d=0일 때
        if len(dessert_type) > ans:         # ans와 길이비교
            ans = len(dessert_type)

        return

    row, col = v

    if G[row][col] in dessert_type:     # 이미 먹어본 디저트면
        return                          # 안 감

    dessert_type.append(G[row][col])    # 일단 가보고

    new_r1 = row + dr[d % 4]            # 그 방향 그대로
    new_c1 = col + dc[d % 4]

    if 0 <= new_r1 < N and 0 <= new_c1 < N:  # 범위 안에 있으면
        cafe_tour(d, (new_r1, new_c1))      # 카페 투어

    new_r2 = row + dr[(d+1) % 4]        # 90도 꺾어서
    new_c2 = col + dc[(d+1) % 4]        # ex> 남서->남동, 남동->북동

    if 0 <= new_r2 < N and 0 <= new_c2 < N:
        cafe_tour(d+1, (new_r2, new_c2))

    dessert_type.pop()                  # 여기 못가는 길이네


for tc in range(int(input())):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    ans = -1

    for r in range(N):
        for c in range(N):
            dessert_type = []
            start_point = (r, c)
            cafe_tour(0, start_point)  # d, v
            # break

        # break
    print('#{} {}'.format(tc+1, ans))
    # break
