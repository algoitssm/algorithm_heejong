# https://www.acmicpc.net/problem/1931

N = int(input())

meetings = []

i = 0
while i < N:
    meeting = list(map(int, input().split()))
    meetings.append(meeting)
    i += 1

meetings.sort(key = lambda x: (x[1], x[0]))

cnt = 0
finish_time = 0

for meeting in meetings:
    if meeting[0] >= finish_time:
        finish_time = meeting[1]
        cnt += 1

print(cnt)