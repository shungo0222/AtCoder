import math

a, b = input().split()
if str(math.sqrt(int(a+b))).split('.')[1] == '0':
    print('Yes')
else:
    print('No')