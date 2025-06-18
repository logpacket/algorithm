n = int(input())
i = 1
while sum(list(range(1, i + 1))) < n:
    i += 1

if i % 2 == 0:
    m = i
    g = 1
else:
    g = i
    m = 1

base = sum(list(range(1, i)))
for j in range(base + 1, n):
    if i % 2 == 0:
        m -= 1
        g += 1
    else:
        m += 1
        g -= 1

print("%d/%d" % (g, m))
