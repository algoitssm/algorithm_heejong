T = int(input())

i = 1
while i <= T:
    n = int(input())
    ans = 0

    while n > 0:
        ans += (-1) ** (n+1) * n
        n -= 1
        
    print(f'#{i} {ans}')

    i += 1
