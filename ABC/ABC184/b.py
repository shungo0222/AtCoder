n, x = map(int, input().split())
s = input()

for i in s:
    if i == 'o':
        x += 1
    elif x > 0 and i == 'x':
        x -= 1

print(x)