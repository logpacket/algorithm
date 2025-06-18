n, m = map(int, input().split())
no_hear = {input() for _ in range(n)}
no_see = {input() for _ in range(m)}
result = sorted(no_hear & no_see)
print(len(result))
for dbj in result:
    print(dbj)
