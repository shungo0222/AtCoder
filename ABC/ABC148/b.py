n = int(input())
S, T = map(list, input().split())
str = ''
for s, t in zip(S, T):
    str += (s + t)
print(str)