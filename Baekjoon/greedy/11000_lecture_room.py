# https://www.acmicpc.net/problem/11000

import sys
import heapq    # 우선순위 큐 사용 필요

N = int(sys.stdin.readline())
times = []

for _ in range(N):
    times.append(tuple(map(int, sys.stdin.readline().split())))

times.sort()    # 강의 시작시간 기준 정렬

t_list = []
heapq.heappush(t_list, 0)    # 강의가 끝나는 시간을 담을 리스트
cnt = 1         # 강의실 개수 하나로 시작
min_index = 0

for time in times:
    # earliest_finish_t = min(t_list)
    earliest_finish_t = t_list[min_index]   # 제일 빨리 끝나는 강의실

    if time[0] < earliest_finish_t:     # 시작시간이 끝나기 전이면
        cnt += 1                        # 강의실 +1
        heapq.heappush(t_list, time[1])          # 끝나는 시간 리스트에 추가

    else:                               # 시작시간이 알맞으면
        # t_list[min_index] = time[1]     # 그 강의실 끝나는 시간 교체
        heapq.heappop(t_list)
        heapq.heappush(t_list, time[1])

    # min_index = t_list.index(min(t_list))   # 제일 빨리 끝나는 강의실로 갱신
    # print(t_list)

print(cnt)
