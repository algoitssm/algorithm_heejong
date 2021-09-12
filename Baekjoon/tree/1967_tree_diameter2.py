# https://www.acmicpc.net/problem/1967
# Unsolved

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# def find_distance()


def find_max_distance(v, cum):
    global my_max
    global node

    if cum > my_max:
        my_max = cum
        node = v
        return

    visited[v] = 1

    for c in tree[v]:
        w = c[0]
        d = c[1]
        if not visited[w]:
            cum += d
            print('w, cum:', w, cum)
            find_max_distance(w, cum)
            cum -= d


n = int(input())
tree = [[] for _ in range(n+1)]    # [자식, 가중치]

for _ in range(n-1):
    p, c, weight = map(int, input().split())
    tree[p].append((c, weight))
    tree[c].append((p, weight))

my_max = 0  # ....?
node = 1
visited = [0 for _ in range(n+1)]
find_max_distance(1, 0)
print(node)

visited = [0 for _ in range(n+1)]
find_max_distance(node, 0)
print(node, my_max)
