n, m = map(int, input().split())
cards = list(map(int, input().split()))

sums = []
for c1 in cards:
    for c2 in cards:
        if c1 == c2:
            continue
        for c3 in cards:
            if c1 == c3 or c2 == c3:
                continue
            sum = c1 + c2 + c3
            if m < sum:
                continue
            sums.append(sum)

print(max(sums))
