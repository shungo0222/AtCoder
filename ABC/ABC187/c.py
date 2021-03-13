n = int(input())
zero, one = set(), set()
for _ in range(n):
    tmp = input()
    if '!' in tmp:
        one.add(tmp[1:])
    else:
        zero.add(tmp)

if len(zero & one) != 0:
    print(list(zero & one)[0])
else:
    print('satisfiable')