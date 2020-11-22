n = int(input())
s = input()

t = []
for i in range(n):
    t.append(s[i])
    if len(t) >= 3 and ''.join(t[-3:]) == 'fox':
        for _ in range(3):
            t.pop()

print(len(t))