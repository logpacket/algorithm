N = int(input())
distances = map(int, input().split())
price = map(int, input().split())

min_price = int(1e9)
total_price = 0
for d, p in zip(distances, price):
    if min_price > p:
        min_price = p

    total_price += min_price * d
print(total_price)
