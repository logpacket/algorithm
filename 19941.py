N, K = map(int, input().split())

table = input()

count = 0
for i, o in enumerate(table):
    if o == "H":
        continue
    for j in range(i - K if i - K > 0 else 0, i + K + 1 if i + K < N else N):
        if table[j] == "H":
            table = table[:j] + "X" + table[j + 1 :]
            count += 1
            break

print(count)
