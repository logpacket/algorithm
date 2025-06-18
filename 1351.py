dp = {0: 1}
N, P, Q = map(int, input().split())


def f(n):
    if n in dp:
        return dp[n]
    dp[n] = f(n // P) + f(n // Q)
    return dp[n]


print(f(N))
