prime = [False] * 100001
count = [0] * 100001
prime[0] = prime[1] = True
for i in range(2, 100001):
    if prime[i]:
        continue
    for j in range(2 * i, 100001, i):
        prime[j] = True
        tmp = j
        while tmp % i == 0:
            tmp //= i
            count[j] += 1


A, B = map(int, input().split())

cnt = 0
for i in range(A, B + 1):
    if not prime[count[i]]:
        cnt += 1

print(cnt)
