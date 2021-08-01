T = int(input())

i = 1
while i <= T:

    N, K = map(int, input().split())

    scores = []
    grade_list = [
        'A+', 'A0', 'A-', 'B+', 'B0',
        'B-', 'C+', 'C0', 'C-', 'D0',
    ]
    
    j = 0
    while j < N:
        mid, final, asmnt = map(int, input().split())
        scores.append(round(0.35*mid + 0.45*final + 0.2*asmnt,2))
        j += 1

    scores_sort = sorted(scores)[::-1]

    score_rank = scores_sort.index(scores[K-1])
    
    grade_index = score_rank // (N // 10)

    ans = grade_list[grade_index]

    print(f'#{i} {ans}')

    i += 1