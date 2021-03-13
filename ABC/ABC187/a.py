a, b = input().split()
s = lambda x: sum(map(int, list(x)))
print(max(s(a), s(b)))