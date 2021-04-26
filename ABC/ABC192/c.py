n, k = input().split()
for i in range(int(k)):
    l = list(n)
    n = str(int(''.join(sorted(l, reverse=True))) - int(''.join(sorted(l))))
print(n)