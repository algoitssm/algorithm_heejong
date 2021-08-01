# Recursion!!!

def pascal_tri(n):
    ans = 1

    if n == 1:
        return [ans]
    elif n == 2:
        return [ans, ans]
    else:
        ans_list = pascal_tri(2)
        idx = 1
        while idx < n-1:
            ans_list.insert(idx, pascal_tri(n-1)[idx-1] + pascal_tri(n-1)[idx])
            idx += 1
        return ans_list

# print(pascal_tri(1))
# print(pascal_tri(2))
# print(pascal_tri(3))
# print(pascal_tri(4))

T = int(input())

i = 0
while i < T:
    N = int(input())
    
    print(f'#{i+1}')
    n = 1
    while n <= N:
        for e in pascal_tri(n):
            print(e, end = ' ')
        print()
        n += 1

    i += 1