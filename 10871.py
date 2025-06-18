N = int(input())
arr = map(int, input().split())

max = -1_000_000
min = 1_000_000
for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

print(min, max)
