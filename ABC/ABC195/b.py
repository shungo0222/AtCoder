import math

a, b, w = map(int, input().split())
upper = math.floor(1000*w/a)
lower = math.ceil(1000*w/b)

if lower > upper:
    print('UNSATISFIABLE')
else:
    print(lower, upper)