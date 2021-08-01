T = int(input())

i = 1
while i <= T:
    st = input()
    chk = 1

    j = 0
    while j < len(st)//2:
        if st[j] != st[-(j+1)]:
            chk = 0
            break
        j += 1
        
    print(f'#{i} {chk}')

    i += 1
