# https://www.acmicpc.net/problem/13549
import sys
from collections import deque
input = sys.stdin.readline


def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1

    if n == K:
        return visited[n]

    while q:

        v = q.popleft()

        w_tp = 2 * v
        if w_tp <= 100001:
            if not visited[w_tp]:
                visited[w_tp] = visited[v]

                if w_tp == K:
                    return visited[w_tp]

                q.append(w_tp)
            w_tp *= 2

        w1 = v - 1
        w2 = v + 1

        if w1 >= 0:

            if not visited[w1]:

                visited[w1] = visited[v] + 1

                if w1 == K:
                    return visited[w1]
                q.append(w1)

        if w2 <= 100000:

            if not visited[w2]:

                visited[w2] = visited[v] + 1

                if w2 == K:
                    return visited[w2]
                q.append(w2)


N, K = map(int, input().split())

visited = [0 for _ in range(100000 + 1)]

print(bfs(N)-1)   # 0초에서 시작하므로
