N = int(input())


graph: list[list[int]] = [
    [idx for idx, ch in enumerate(input()) if ch == "Y"] for _ in range(N)
]

max_firends = 0
for i in range(N):
    friends = set(graph[i])
    for f in graph[i]:
        for f2 in graph[f]:
            friends.add(f2)

    try:
        friends.remove(i)
    except KeyError:
        pass
    if max_firends < len(friends):
        max_firends = len(friends)

print(max_firends)
