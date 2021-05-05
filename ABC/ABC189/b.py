n, x = map(int, input().split())
alcho = 0
for i in range(n):
    v, p = map(int, input().split())
    alcho += v * p
    if alcho > x * 100:
        print(i+1)
        exit()
print(-1)