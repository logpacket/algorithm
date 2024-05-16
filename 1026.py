import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0

while len(B) != 0:
    max_b = B.pop(B.index(max(B)))
    min_a = A.pop(A.index(min(A)))

    result += max_b * min_a

print(result)
