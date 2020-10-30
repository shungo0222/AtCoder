n, m = map(int, input().split())
a = [int(i) for i in input().split()]
days = sum(a)

if n - days >= 0:
    print(n - days)
else:
    print(-1)