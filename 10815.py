n = int(input())
owns = set(map(int, input().split()))
m = int(input())
M = map(int, input().split())

for i in M:
    if i in owns:
        print(1, end=" ")
    else:
        print(
            0,
            end=" ",
        )
