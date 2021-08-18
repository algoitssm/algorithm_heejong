# https://www.acmicpc.net/problem/1541

# 처음에 빼기가 나올 때까지는 다 더하고 빼기가 나온 이후로는 연산자에 상관없이 뺌

origin_list = list(input())

ans = 0
chk = 1             # 처음에는 부호 +
tmp_num_str = ""    # 숫자를 누적해서 담을 문자열

for idx in range(len(origin_list)):

    try:
        tmp_num_str += str(int(origin_list[idx]))   # 숫자와 연산자를 구분하기 위함
    except:                                         # 연산자면
        ans += chk * int(tmp_num_str)               # 이때까지 나온 숫자를 계산함
        if origin_list[idx] == "-":                 # 빼기가 나오면
            chk = -1                                # 부호 -
        tmp_num_str = ""                            # 누적 숫자 초기화

else:
    ans += chk * int(tmp_num_str)                   # 마지막에는 남은 숫자들 처리

print(ans)
