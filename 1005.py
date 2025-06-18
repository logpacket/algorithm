from collections import defaultdict

memo: dict[int, int] = {}


def calc_duration(
    ds_map: dict[int, int],
    depends: dict[int, list[int]],
    x: int,
) -> int:
    if memo.get(x) is not None:
        return memo[x]
    if len(depends[x]) == 0:
        return ds_map[x]
    memo[x] = ds_map[x] + max([calc_duration(ds_map, depends, d) for d in depends[x]])
    return memo[x]


T = int(input())
for k in range(T):
    N, K = map(int, input().split())
    build_ds = map(int, input().split())
    build_ds_map = {idx + 1: ds for idx, ds in enumerate(build_ds)}

    build_depends = defaultdict(list)
    for i in range(K):
        a, b = map(int, input().split())
        build_depends[b].append(a)
    W = int(input())
    print("output:", calc_duration(build_ds_map, build_depends, W))
