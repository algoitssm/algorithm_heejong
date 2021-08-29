# https://www.acmicpc.net/problem/2564

W, H = map(int, input().split())

N = int(input())

shops = [[] for _ in range(4 + 1)]
for _ in range(N):
    side, dist = map(int, input().split())
    shops[side].append(dist)

my_spot = list(map(int, input().split()))

my_side = my_spot[0]

# print(shops)
# print(my_spot)

dist_sum = 0
for d in range(len(shops)):
    for shop_dist in shops[d]:

        if my_side == 1:

            if d == 1:
                if my_spot[1] > shop_dist:
                    dist_sum += my_spot[1] - shop_dist
                else:
                    dist_sum += shop_dist - my_spot[1]

            elif d == 2:
                dist_sum += H

                if my_spot[1] + shop_dist > W:
                    dist_sum += (W - my_spot[1]) + (W - shop_dist)
                else:
                    dist_sum += my_spot[1] + shop_dist

            elif d == 3:

                dist_sum += my_spot[1] + shop_dist

            elif d == 4:

                dist_sum += (W - my_spot[1]) + shop_dist

        if my_side == 2:

            if d == 2:
                if my_spot[1] > shop_dist:
                    dist_sum += my_spot[1] - shop_dist
                else:
                    dist_sum += shop_dist - my_spot[1]

            elif d == 1:
                dist_sum += H

                if my_spot[1] + shop_dist > W:
                    dist_sum += (W - my_spot[1]) + (W - shop_dist)
                else:
                    dist_sum += my_spot[1] + shop_dist

            elif d == 3:

                dist_sum += my_spot[1] + (H - shop_dist)

            elif d == 4:

                dist_sum += (W - my_spot[1]) + (H - shop_dist)

        if my_side == 3:

            if d == 3:
                if my_spot[1] > shop_dist:
                    dist_sum += my_spot[1] - shop_dist
                else:
                    dist_sum += shop_dist - my_spot[1]

            elif d == 4:
                dist_sum += W

                if my_spot[1] + shop_dist > H:
                    dist_sum += (H - my_spot[1]) + (H - shop_dist)
                else:
                    dist_sum += my_spot[1] + shop_dist

            elif d == 1:
                dist_sum += my_spot[1] + shop_dist

            elif d == 2:
                dist_sum += (H - my_spot[1]) + shop_dist

        if my_side == 4:

            if d == 4:
                if my_spot[1] > shop_dist:
                    dist_sum += my_spot[1] - shop_dist
                else:
                    dist_sum += shop_dist - my_spot[1]

            elif d == 3:
                dist_sum += W

                if my_spot[1] + shop_dist > H:
                    dist_sum += (H - my_spot[1]) + (H - shop_dist)
                else:
                    dist_sum += my_spot[1] + shop_dist

            elif d == 1:
                dist_sum += my_spot[1] + (W - shop_dist)

            elif d == 2:
                dist_sum += (H - my_spot[1]) + (W - shop_dist)

print(dist_sum)
