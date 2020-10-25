a, b, c, k = list(map(int, input().split()))

max = 0
if(a >= k):
    max = k
else:
    max = a
    k -= a
    if(b >= k):
        pass
    else:
        k -= b
        max -= k

print(max)