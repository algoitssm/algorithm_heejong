# https://www.acmicpc.net/problem/13305

n = int(input())

distances = list(map(int, input().split()))
petroleum_prices = list(map(int, input().split()))


# 58점
# ans = 0

# while True:
#     min_price = min(petroleum_prices[:len(distances)])
#     idx = petroleum_prices.index(min_price)
#     ans += min_price * sum(distances[idx:])

#     if idx == 0:
#         break

#     petroleum_prices = petroleum_prices[:idx+1]
#     distances = distances[:idx]

# print(ans)



# Recursive

# def save_money(dist_list, price_list, ans = 0):
#     idx = price_list.index(min(price_list[:-1]))
#     ans += min(price_list[:-1]) * sum(dist_list[idx:])

#     if not idx:
#         return ans

#     else:
#         return save_money(dist_list[:idx], price_list[:idx+1], ans)

# print(save_money(distances, petroleum_prices))

ans = 0

price = petroleum_prices[0]

for idx in range(len(distances)):
    ans += price * distances[idx]

    if price > petroleum_prices[idx+1]:
        price = petroleum_prices[idx+1]

print(ans)
    
