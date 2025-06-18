import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
space = [list(map(int, input().rstrip().split())) for _ in range(N)]

cost: dict[tuple[int, int], dict[int, int]] = {}


def traversal(x, y, last_direction=None):
    if y == N - 1:
        return space[y][x]
    current_cost = cost.get((x, y), {-1: 0, 0: 0, 1: 0})
    for i in range(-1, 2):
        if 0 <= x + i < M and last_direction != i and current_cost[i] == 0:
            next_cost = space[y][x] + traversal(x + i, y + 1, i)
            current_cost[i] = next_cost

    cost[(x, y)] = current_cost
    return min(
        cost for i, cost in current_cost.items() if (i != last_direction and cost != 0)
    )


costs = [traversal(i, 0) for i in range(M)]
print(min(costs))
