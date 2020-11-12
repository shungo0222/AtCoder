n, k, m = map(int, input().split())
a = [int(i) for i in input().split()]
if 0 < n*m-sum(a) and n*m-sum(a) <= k:
    print(n*m-sum(a))
elif n*m-sum(a) <= 0:
    print(0)
else:
    print(-1)