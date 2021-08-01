T = int(input())

i = 0
while i < T:
    st = input()

    # 1)
    # 다음 문자열의 문자가 만들고 있는 패턴에 없으면 추가
    # SAMSUNG같은 단어에서 두 번 째 S를 추가 x  =>  FAIL
    # for s in st:
    #     if s not in patt:
    #         patt += s
    


    # 2)
    # T의 약수를 찾아서 해당 길이만큼 반복되는 지 확인
    # 계속 못찾음... 포기하고 다른 방법 생각

    # n_list = []
    # j = 1
    # while j <= len(st):
        
    #     if not (len(st) % j):
    #         n_list.append(j)
    #     j += 1
    
    # chk = 0
    # for n in n_list[:-1]:
    #     chk = 0
    #     for m in range(len(st)//n):
    #         print(st[m:m + n],st[m + n:m + 2 * n])
    #         if st[m:m + n + 1] != st[m + n + 1:m + 2 * n + 2]:
    #             break
        
    #     else:
    #         patt = st[:n+1]
    #         chk = 1

    # if chk == 0:
    #     patt_length = len(st)
    # else:
    #     patt_length = len(patt)




    # 3)
    # 각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.
    # 제약사항을 확인하고 다시 생각....
    # 문제를 잘 읽자

    possible_patterns = []

    # 으아ㅏ앙아ㅏㅏㅏㅏㅏㅏ

    # while patt_len <= max_len:
    #     possible_patterns.append(st[:patt_len + 1])

    #     patt_len += 1

    # for possible_pattern in possible_patterns:
    #     tmp = ''
        
    #     for k in range(st_len // len(possible_pattern)):
    #         if possible_pattern != st[k + patt_len: 2 * (k + patt_len)]:
    #             break
    #     else:
    #         tmp = possible_pattern

    #     if len(tmp) < patt:
    #         patt = tmp
    #         break


    # 4) 결국 for문을 남발해봤다..

    for j in range(1, 11):
        possible_patterns.append(st[:j])

    # 길이가 긴 패턴부터 하면 마지막에 저장되는 패턴이 가장 짧음
    for possible_pattern in possible_patterns[::-1]:            # 리스트 역순 정렬을 계속 [:-1]로 실수함

        # 바로 다음 요소 뿐 아니라 문자열 끝까지 확인
        for k in range(len(st) // len(possible_pattern)):       # pattern길이가 2면 (15-1)번, 3이면 (10-1)번, ... , 확인
            if possible_pattern != st[k * len(possible_pattern):(k + 1) * len(possible_pattern)]:
                break
        else:
            patt = possible_pattern
        
        patt_length = len(patt)

    print(f'#{i+1} {patt_length}')
    i += 1