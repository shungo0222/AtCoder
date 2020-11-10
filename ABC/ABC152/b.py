a, b = map(int, input().split())
num = sorted([str(a) * b, str(b) * a])
print(num[0])