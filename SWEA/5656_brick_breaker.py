import sys
sys.stdin = open('input10.txt')

for tc in range(int(input())):
    N, W, H = map(int, input().split())
    G = [list(map(int, input().split())) for _ in range(H)]
    print(G)

    ans = 0
    print('#{} {}'.format(tc+1, ans))
    break
