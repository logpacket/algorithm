import sys

n36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
input = sys.stdin.readline
diffs = [0] * 36


def caldiff(num_str):
    for i, ch in enumerate(num_str):
        num = int(ch, 36)
        diff = (35 - num) * 36 ** ((len(num_str) - i) - 1)
        diffs[num] += diff


def make36(x):
    if x == 0:
        return 0
    dq = []
    while x:
        dq.insert(0, n36[x % 36])
        x //= 36
    return "".join(dq)


N = int(input())

nums: list[str] = []
SUM = 0

for i in range(N):
    num = input().replace("\n", "")
    nums.append(num)
    SUM += int(num, 36)
    diff = caldiff(num)


K = int(input())

diffs.sort(reverse=True)
for i in range(K):
    SUM += diffs[i]


print(make36(SUM))
