N, X = map(int, input().split())
visitors = list(map(int, input().split()))
cumulative_visitors = [0] * N
for i, visitor in enumerate(visitors):
    cumulative_visitors[i] = (
        (cumulative_visitors[i - 1] + visitor) if i > 0 else visitor
    )

sums = [0] * (N - X + 1)
for i in range(X - 1, N):
    sums[i - X + 1] = (
        (cumulative_visitors[i] - cumulative_visitors[i - X])
        if i - X >= 0
        else cumulative_visitors[i]
    )

max_sums = max(sums)
if max_sums == 0:
    print("SAD")
else:
    print(max_sums)
    print(sums.count(max_sums))
