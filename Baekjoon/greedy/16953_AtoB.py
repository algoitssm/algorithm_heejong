# https://www.acmicpc.net/problem/16953

A, B = map(int, input().split())

# print(A, B)

cnt = 1
while True:
    # 거꾸로 B에서 A로 갈 수 있는 지를 생각

    if B == A:  # 같으면
        break   # 계산할 필요가 없음

    if not B % 2 and B > A:  # B가 2로 나누어떨어지고 B가 A보다 크면
        B //= 2             # B를 2로 나눔
    else:                   # 그게 아니면
        if B % 10 == 1:     # B의 끝자리가 1인지 확인
            B //= 10        # 1을 떼어냄

        else:               # 그것도 아니면
            cnt = -1        # A에서 B로 만들 수가 없음
            break

    cnt += 1

print(cnt)
