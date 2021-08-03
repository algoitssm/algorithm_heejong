T = int(input())

i = 1
while i <= T:

    N, K = map(int, input().split())

    scores = []

    # 성적 리스트
    grade_list = [
        'A+', 'A0', 'A-', 'B+', 'B0',
        'B-', 'C+', 'C0', 'C-', 'D0',
    ]
    
    # score 평균
    j = 0
    while j < N:
        mid, final, asmnt = map(int, input().split())
        scores.append(round(0.35*mid + 0.45*final + 0.2*asmnt,2))
        j += 1

    scores_sort = sorted(scores)[::-1]          # scores 내림차순 정렬

    score_rank = scores_sort.index(scores[K-1]) # 내 점수가 몇 등인지
    
    grade_index = score_rank // (N // 10)       # 몇 명씩 같은 등급인지

    ans = grade_list[grade_index]               # 그 인덱스에 해당하는 등급

    print(f'#{i} {ans}')

    i += 1