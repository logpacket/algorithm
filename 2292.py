n = int(input())

i = 1
num_box = 1

while n > num_box:
    num_box += 6 * i
    i += 1

print(i)
