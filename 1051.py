def check_func(vals: list[list[int]], x: int, y: int, size: int):
    val = vals[y][x]
    return all(
        v == val
        for v in [
            vals[y][x + size - 1],
            vals[y + size - 1][x],
            vals[y + size - 1][x + size - 1],
        ]
    )


N, M = map(int, input().split())

vals = []

for i in range(N):
    vals.append(list(map(int, (ch for ch in input()))))

result = 1
MAX_SIZE = min(N, M)
for size in range(2, MAX_SIZE + 1):
    for i in range(N - (size - 1)):
        for j in range(M - (size - 1)):
            if check_func(vals, j, i, size):
                result = size**2


print(result)
