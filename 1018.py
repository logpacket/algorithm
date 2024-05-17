coreect_plateW = [
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
]
coreect_plateB = [
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
]


def calc_repaint(
    plate: list[list[str]],
    start_row: int,
    start_col: int,
) -> int:
    Wcnt = 0
    Bcnt = 0
    for i in range(start_row, start_row + 8):
        for j in range(start_col, start_col + 8):
            if coreect_plateW[i - start_row][j - start_col] != plate[i][j]:
                Wcnt += 1
            if coreect_plateB[i - start_row][j - start_col] != plate[i][j]:
                Bcnt += 1

    return min(Wcnt, Bcnt)


N, M = map(int, input().split())

plate: list[list[str]] = []

for i in range(N):
    plate.append([])
    plate[i] = [ch for ch in input()]


min_cnt = 100
for i in range(N - 7):
    for j in range(M - 7):
        min_cnt = min(min_cnt, calc_repaint(plate, i, j))

print(min_cnt)
