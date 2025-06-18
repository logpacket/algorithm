n = int(input())
office = {}

for i in range(n):
    name, log = input().split()
    if log == "enter":
        office[name] = 1
    elif log == "leave":
        del office[name]

for j in sorted(office.keys(), reverse=True):
    print(j)
