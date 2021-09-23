import sys
sys.stdin = open('input4.txt')

for tc in range(int(input())):
    # 지도 세로, 지도 가로, 뚜껑 세로, 뚜껑 가로, 시간
    N, M, R, C, L = map(int, input().split())

    G = []
    for _ in range(N):
        G.append(list(map(int, input().split())))

    print(G)

    ans = 0
    print('#{0} {1}'.format(tc+1, ans))
    break
