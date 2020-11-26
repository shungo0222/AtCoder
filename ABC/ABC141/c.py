import collections

n, k, q = map(int, input().split())
a = []
for _ in range(q):
    a.append(int(input()))
a = collections.Counter(a)
for i in range(1, n+1):
    if k - (q - a[i]) > 0:
        print('Yes')
    else:
        print('No')