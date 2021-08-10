# https://www.acmicpc.net/problem/1541

origin_list = list(input())

ans = 0
chk = 1
tmp_num_str = ""

for idx in range(len(origin_list)):

    try:
        tmp_num_str += str(int(origin_list[idx]))
    except:
        ans += chk * int(tmp_num_str)
        if origin_list[idx] == "-":
            chk = -1
        tmp_num_str = ""

else:
    ans += chk * int(tmp_num_str)

print(ans)
