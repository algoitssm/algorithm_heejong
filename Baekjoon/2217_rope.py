n = int(input())
input_num_list = []
ans_list = []

i = 0
while i < n:

    input_num_list.append(int(input()))
    # ans_list.append(min(input_num_list) * (i + 1))
    i += 1

input_num_list.sort(reverse=True)
my_max = input_num_list[0]
j = 0
while j < n:
    if my_max < input_num_list[-1] * len(input_num_list):
        my_max = input_num_list[-1] * len(input_num_list)
    input_num_list.pop()
    j += 1

print(my_max)
