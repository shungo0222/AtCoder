n = int(input())
a = [int(i) for i in input().split()]
set_a = set(a)
if len(set_a) == n:
    print('YES')
else:
    print('NO')