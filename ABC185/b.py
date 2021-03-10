n, m, t = map(int, input().split())
n_max = n

b_tmp = 0
for i in range(m):
    a, b = map(int, input().split())
    
    if i == 0:
        n -= a
    else:
        n -= a - b_tmp
    b_tmp = b
    
    if n <= 0:
        print('No')
        exit()
        
    n += b - a
    if n > n_max:
        n = n_max
    
    if i == m - 1:
        n -= t - b

if n <= 0:
    print('No')
else:
    print('Yes')