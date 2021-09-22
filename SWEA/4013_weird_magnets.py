# import sys
from collections import deque
# sys.stdin = open('input2.txt')


def rotate(num, rotate_type):   # 회전 함수
    if rotate_type == 1:    # 시계방향
        magnets[num].appendleft(magnets[num].pop())
    else:       # 반시계방향
        magnets[num].append(magnets[num].popleft())


def check_magnets(num):  # 같이 회전할 자석을 찾는 함수

    nums.append(num)    # nums 에 저장하고
    visited[num] = 1    # 방문처리

    if num == 0:    # 맨 왼쪽 0일 때
        chk_num = num + 1   # 오른쪽 확인
        if not visited[chk_num]:
            if magnets[num][2] != magnets[chk_num][6]:
                check_magnets(chk_num)

    elif num == 3:  # 맨 오른쪽 3일 때
        chk_num = num - 1   # 왼쪽 확인
        if not visited[chk_num]:
            if magnets[num][6] != magnets[chk_num][2]:
                check_magnets(chk_num)

    else:   # 사이에 있는 번호면
        chk_num1 = num - 1  # 왼쪽 확인
        if not visited[chk_num1]:
            if magnets[num][6] != magnets[chk_num1][2]:
                check_magnets(chk_num1)

        chk_num2 = num + 1  # 오른쪽 확인
        if not visited[chk_num2]:
            if magnets[num][2] != magnets[chk_num2][6]:
                check_magnets(chk_num2)


for tc in range(int(input())):
    K = int(input())

    magnets = []
    for _ in range(4):
        magnets.append(deque(map(int, input().split())))

    # print(magnets)
    for _ in range(K):
        magnet_num, rotate_type = map(int, input().split())
        magnet_num -= 1  # 인덱스라서 하나 빼줌

        visited = [0 for _ in range(4)]  # dfs
        nums = []   # 같이 회전하는 자석을 저장

        check_magnets(magnet_num)   # 같이 회전할 자석을 찾자

        for num in nums:
            if magnet_num % 2 == num % 2:   # ex> magnet_num=1 일 때 1, 3
                rotate(num, rotate_type)    # 같은 방향 회전
            else:                           # ex> magnet_num=1 일 때 2, 4
                rotate(num, rotate_type * (-1))  # 반대로 회전

        # print(magnets)
        # break

    ans = 0
    for i in range(4):  # 점수 계산
        ans += magnets[i][0] * (2 ** i)

    print(f'#{tc+1} {ans}')
    # break
