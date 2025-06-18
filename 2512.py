N = int(input())
requests = list(map(int, input().split()))
total = int(input())

sum_requests = sum(requests)
if sum_requests <= total:
    print(max(requests))
else:
    left = 0
    right = max(requests)
    while left <= right:
        mid = (left + right) // 2
        total_requests = sum([min(request, mid) for request in requests])
        if total_requests > total:
            right = mid - 1
        else:
            left = mid + 1
    print(right)
