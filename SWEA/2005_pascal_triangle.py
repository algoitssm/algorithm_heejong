# Recursion!!!

def pascal_tri(n):
    ans = 1

    if n == 1:              # 1이면
        return [ans]        # [1] 반환
    elif n == 2:            # 2이면
        return [ans, ans]   # [1, 1] 반환
    else:                   # 그 외에는
        ans_list = pascal_tri(2)    # [1,1]
        idx = 1                     # 인덱스 변수 설정 (1부터 시작)
        while idx < n-1:            # 인덱스 변수를 하나씩 증가시킬 때마다
            ans_list.insert(idx, pascal_tri(n-1)[idx-1] + pascal_tri(n-1)[idx]) # 파스칼 삼각형 윗 행의 두 수를 더해서 삽입
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