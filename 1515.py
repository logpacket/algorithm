nums = input()

n = 0
i = 0
while True:
    n += 1
    for s in str(n):
        if nums[i] == s:
            i += 1
            if i >= len(nums):
                print(n)
                exit()
