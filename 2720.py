T = int(input())

coins = [25, 10, 5, 1]

for i in range(T):
    C = int(input())

    for coin in coins:
        print(C // coin, end=" ")
        C %= coin

    print()
