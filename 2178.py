N, M = map(int, input().split())
G = [list(map(int, input())) for _ in range(N)]


# Find the least distance between from (0, 0) to (N-1, M-1)
def bfs():
    queue = [(0, 0)]
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    distance = 0

    while queue:
        next_queue = []
        for x, y in queue:
            if x == N - 1 and y == M - 1:
                return distance
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if (
                    0 <= ny < M
                    and 0 <= nx < N
                    and G[nx][ny] == 1
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = True
                    next_queue.append((nx, ny))
        queue = next_queue
        distance += 1

    return -1


print(bfs() + 1)
