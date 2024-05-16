N, M, V = map(int, input().split())

graph: dict[int, list[int]] = {}

for i in range(M):
    a, b = map(int, input().split())
    if graph.get(a) is None:
        graph[a] = []
    graph[a].append(b)
    if graph.get(b) is None:
        graph[b] = []
    graph[b].append(a)

graph = {k: sorted(v) for k, v in graph.items()}


def bfs(graph: dict[int, list[int]]) -> None:
    checked = set()
    queue = [V]

    while len(queue) != 0:
        node = queue.pop()
        checked.add(node)
        print(node, end=" ")
        nodes = graph.get(node)
        if nodes is None:
            continue
        for n in nodes:
            if n not in checked and n not in queue:
                queue.insert(0, n)


def dfs(graph: dict[int, list[int]], node: int, checked: set[int]) -> None:
    checked.add(node)
    print(node, end=" ")
    nodes = graph.get(node)
    if nodes is None:
        return
    for n in nodes:
        if n not in checked:
            dfs(graph, n, checked)


dfs(graph, V, set())
print()
bfs(graph)
