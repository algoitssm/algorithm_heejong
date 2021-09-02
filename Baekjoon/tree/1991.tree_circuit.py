# https://www.acmicpc.net/problem/1991

def pre_order(char):
    if char != '.':
        print(char, end='')
        pre_order(tree[char][0])
        pre_order(tree[char][1])


def in_order(char):
    if char != '.':
        in_order(tree[char][0])
        print(char, end='')
        in_order(tree[char][1])


def post_order(char):
    if char != '.':
        post_order(tree[char][0])
        post_order(tree[char][1])
        print(char, end='')


N = int(input())

tree = {}
for _ in range(N):
    me, left, right = input().split()
    tree[me] = (left, right)

# print(tree)
pre_order('A')
print()
in_order('A')
print()
post_order('A')
