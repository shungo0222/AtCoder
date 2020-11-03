n = int(input())

a = int(n/500)
b = n - 500*a
b = int(b/5)

print(a*1000 + b*5)