# https://www.acmicpc.net/problem/1758

n = int(input())

tip_list = []
while n > 0:
    tip_list.append(int(input()))
    n -= 1

tip_list.sort(reverse=True)

my_sum = 0
idx = 0

while idx < len(tip_list):
    if tip_list[idx] - idx > 0:
        my_sum += tip_list[idx] - idx
    idx += 1

# while tip_list[idx] - idx > 0:
#     my_sum += tip_list[idx] - idx
    
#     if tip_list[idx] - idx < 0:
#         break
#     idx += 1

print(my_sum)