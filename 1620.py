import sys

input = sys.stdin.readline
n, m = map(int, input().split())

name_to_num = {}
num_to_name = {}

for i in range(1, n + 1):
    name = input().rstrip()
    name_to_num[name] = i
    num_to_name[i] = name

for i in range(m):
    query = input().rstrip()
    if query.isdigit():
        print(num_to_name[int(query)])
    else:
        print(name_to_num[query])
