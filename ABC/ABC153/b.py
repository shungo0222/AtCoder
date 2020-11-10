h, n = map(int, input().split())
a = [int(i) for i in input().split()]
if sum(a) >= h:
    print('Yes')
else:
    print('No')