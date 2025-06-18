def str_to_int(n):
    if n.isdigit():
        return int(n)
    else:
        return ord(n) - 55


def int_to_str(ch):
    if ch < 10:
        return str(ch)
    else:
        return chr(ch + 55)


N, b = input().split()
B = int(b)

result = 0
length = len(N)
for i in range(length - 1, -1, -1):
    result += str_to_int(N[i]) * B ** (length - i - 1)

print(result)
