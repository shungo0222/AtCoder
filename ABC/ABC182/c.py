n = list(map(int, list(input())))
n_len = len(n)

digit = 20
for i in range(2 ** n_len - 1):
    toggle = [1] * n_len
    for j in range(n_len):
        if (i >> j) & 1:
            toggle[j] = 0
    
    tmp = 0
    for k in range(n_len):
        if toggle[k]:
            tmp += n[k]
    if tmp % 3 == 0:
        digit = min(digit, toggle.count(0))

if digit == 20:
    print(-1)
else:
    print(digit)