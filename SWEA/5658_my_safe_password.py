
for tc in range(int(input())):
    N, K = map(int, input().split())
    letters_per_side = N // 4   # 변당 문자 수

    string = input() * 2    # 인덱스 생각하고 싶지 않아서 *2 (이게 되네?)
    # 1B3B3B81F75E + 1B3B3B81F75E

    # 회전 시작
    cases = []  # 나올 수 있는 케이스를 담자
    for rotate_num in range(letters_per_side):  # 변당 문자 수만큼만 돌면 됨

        # 앞부분 구분점. 시계방향으로 돈 다는 것은 구분점이 한칸씩 당겨진다는 의미
        former_compartment = N - rotate_num  # 인덱스가 N인 지점부터 시작

        while former_compartment <= N * 2 - letters_per_side:   # 끝에까지 셀 수 있게 조정
            latter_compartment = former_compartment + letters_per_side  # 뒷부분 구분점
            cases.append(
                int(string[former_compartment:latter_compartment], 16))  # 16진수 문자열을 10진수 숫자로 변환해서 저장

            former_compartment = latter_compartment  # 앞부분 구분점 이동

    cases = sorted(list(set(cases)), reverse=True)  # 큰 수 기준 내림차순 정렬

    ans = cases[K-1]    # K'번째'라서 -1
    print(f'#{tc+1} {ans}')
    # break
