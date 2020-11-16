n = int(input())
s = list(input())
string = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2)
for i in range(len(s)):
    s[i] = string[string.index(s[i])+n]
print(*s, sep='')