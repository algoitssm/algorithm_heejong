T = int(input())

i = 1
while i <= T:
    
    my_list = list(map(int, input().split()))

    my_list.remove(max(my_list))
    my_list.remove(min(my_list))


    ans = round(sum(my_list)/len(my_list))

        
    print(f'#{i} {ans}')

    i += 1