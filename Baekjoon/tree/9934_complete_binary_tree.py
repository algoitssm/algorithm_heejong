# https://www.acmicpc.net/problem/9934
import math


def put_center_num(lst: list, i: int):
    center_idx = len(lst)//2    # 가운데 인덱스

    ans_list[i].append(lst[center_idx])  # 0번째 레벨에는 가운데 인덱스 숫자 put

    if center_idx == 0:  # 가운데 인덱스가 0이면 == 빈 리스트이면
        return

    put_center_num(lst[:center_idx], i+1)   # 좌측 서브트리
    put_center_num(lst[center_idx+1:], i+1)  # 우측 서브트리


K = int(input())
visit_list = list(map(int, input().split()))

N = len(visit_list)             # 노드의 개수

level = int(math.log2(N + 1))   # log2(노드의 개수 + 1)로 트리 깊이를 계산

ans_list = [[] for _ in range(level)]   # 각 깊이 별로 빌딩을 담을 리스트

cnt = 0
put_center_num(visit_list, cnt)  # 가운데 번호를 넣자

for j in range(level):
    print(*ans_list[j])
