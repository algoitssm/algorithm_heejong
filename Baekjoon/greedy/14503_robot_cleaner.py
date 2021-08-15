# https://www.acmicpc.net/problem/14503

n, m = map(int, input().split())
r, c, d = map(int, input().split())

map_to_clean = []

while n > 0:
    map_to_clean.append(list(map(int, input().split())))
    n -= 1

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

# 1. 현재 위치를 청소
map_to_clean[r][c] = 2
cnt = 1

def clean(r, c, d, map_clean, cnt):

    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색
    i = 1
    while i <= 4:

        # 왼쪽 방향
        d_left = (d-1) % 4

        # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면
        if map_clean[r+dr[d_left]][c+dc[d_left]] == 0:

            # 1번부터 진행 (이 부분이 빠지면 무한재귀)
            map_clean[r+dr[d_left]][c+dc[d_left]] = 2
            cnt += 1

            return clean(r+dr[d_left], c+dc[d_left], d_left, map_clean, cnt)
        
        # b. 왼쪽 방향에 청소할 공간이 없다면
        # elif map_clean[r+dr[d]][c+dc[d]] != 0:

        # 그 방향으로 회전
        d = d_left
        
        i += 1

    # c. 네 방향 모두 청소가 이미 되어있거나 벽이면
    else:
        # 바라보는 방향을 유지한 채로 한 칸 후진을 하고 
        if map_clean[r-dr[d]][c-dc[d]] == 2:

            # 2번으로 돌아감
            return clean(r-dr[d], c-dc[d], d, map_clean, cnt)

        # d. 뒤 쪽이 벽이면
        else:
            # 작동 멈춤
            return cnt

print(clean(r, c, d, map_to_clean, cnt))