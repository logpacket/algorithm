import sys

input = sys.stdin.readline

T = int(input())


def counting_bundles(coords: list[tuple[int, int]]) -> int:
    bundle_cnt = 0
    while len(coords) != 0:
        queue: list[tuple[int, int]] = []

        start = coords.pop()
        queue.append(start)

        while len(queue) != 0:
            coord = queue.pop()
            adjs = [
                (coord[0], coord[1] + 1),
                (coord[0], coord[1] - 1),
                (coord[0] - 1, coord[1]),
                (coord[0] + 1, coord[1]),
            ]
            queue.extend(
                map(
                    lambda adj: coords.pop(coords.index(adj)),
                    [adj for adj in adjs if adj in coords],
                )
            )
        bundle_cnt += 1

    return bundle_cnt


for i in range(T):
    coords = []
    M, N, K = map(int, input().split())
    for j in range(K):
        coords.append(tuple(map(int, input().split())))
    print(counting_bundles(coords))  # type: ignore
