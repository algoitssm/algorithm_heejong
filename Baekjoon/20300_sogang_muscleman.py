# https://www.acmicpc.net/problem/20300

n = int(input())

t = list(map(int, input().split()))
t.sort()                # 정렬

max_num = 0

if len(t) & 1:          # 홀수이면
    max_num = t.pop()   # 제일 큰 수를 저장

odd_idx_list = t[::2]           # ex> [1,2,3,4,5,6] => [1,3,5]
even_idx_list_reverse = t[-1::-2]   # [1,2,3,4,5,6] => [6,4,2]

for i in range(len(odd_idx_list)):
    if max_num < odd_idx_list[i] + even_idx_list_reverse[i]:
        max_num = odd_idx_list[i] + even_idx_list_reverse[i]

print(max_num)