# https://www.acmicpc.net/problem/17829


def validate(adj):

    if len(adj) == 1:       # 1x1이면
        return adj[0][0]    # 그 값 반환

    else:                   # 계속 나누어야하면
        n_adj = []          # 축소시킨 그래프 생성

        for r in range(0, len(adj), 2):         # 행 2씩 증가시키면서
            each_row = []   # 축소시킨 그래프의 한 행

            for c in range(0, len(adj), 2):     # 열 2씩 증가시키면서
                # 2x2 행렬이 만들어짐

                tmp_num = []
                for inner_r in range(r, r+2):           # 2x2 전체 탐색
                    for inner_c in range(c, c+2):
                        tmp_num.append(adj[inner_r][inner_c])   # 모든 원소를 한 리스트로

                # 그 중 두번째로 큰 수를 행에 계속 추가
                each_row.append(max(sorted(tmp_num)[:-1]))

            n_adj.append(each_row)  # 행 전체를 다음 그래프에 추가

        return validate(n_adj)      # 재귀탐색


N = int(input())

G = [list(map(int, input().split())) for _ in range(N)]

print(validate(G))
