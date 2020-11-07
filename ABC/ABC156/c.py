n = int(input())
x = list(map(int, input().split()))
p = round(sum(x)/n)
stamina = 0
for i in range(n):
    stamina += (x[i] - p) ** 2
print(stamina)