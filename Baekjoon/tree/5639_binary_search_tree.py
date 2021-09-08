# https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit(100000)


def pre_to_post_order(lst: list):

    if not lst:  # 리스트가 비면
        return

    pivot = lst[0]  # 리스트 첫번째 값 기준

    for idx in range(1, len(lst)):  # 기준 제외 리스트 전체 순회
        if lst[idx] > pivot:        # 기준 보다 큰 값이 나오면
            pre_to_post_order(lst[1:idx])   # 그 값 이전까지 재귀
            pre_to_post_order(lst[idx:])    # 그 이후로는 따로 재귀
            ans.append(pivot)       # 기준은 마지막에 추가
            return

    pre_to_post_order(lst[1:])      # 전체 다 기준보다 작을 경우
    ans.append(pivot)               # 기준은 마지막에 추가


nums = []
while True:
    try:
        num = input()
        nums.append(int(num))
    except:     # 에러가 나면
        break   # 입력 끝

ans = []
pre_to_post_order(nums)  # 숫자 리스트를 전위에서 후위 순회로
print(*ans, sep='\n')   # 출력 형식 맞춤
