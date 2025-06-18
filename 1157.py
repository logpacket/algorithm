string = input().upper()

dic = {}
for i in string:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

m = max(dic.values())
count = 0
maxAlpha = ""
for k, v in dic.items():
    if v == m:
        count += 1
        maxAlpha = k

if count > 1:
    print("?")
else:
    print(maxAlpha)
