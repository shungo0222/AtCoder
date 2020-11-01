n, m = map(int, input().split())
products = [int(i) for i in input().split()]
get = [j for j in products if j >= (sum(products) * (1 / (4*m)))]
if len(get) >= m:
    print('Yes')
else:
    print('No')