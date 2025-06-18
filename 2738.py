N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
for i, v in enumerate(map(int, input().split())):
    for j in range(M):
        print(X[i][j] + v, end=" ")
    print()
