memo = {0: 0, 1: 1}


def fibo(n: int) -> int:
    memoed = memo.get(n)
    if memoed is not None:
        return memoed

    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]


n = int(input())
print(fibo(n))
