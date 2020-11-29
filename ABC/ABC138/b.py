from fractions import Fraction

n = int(input())
a = list(map(int, input().split()))
deno = 0
for i in a:
    deno += Fraction(1, i)
print(float(1/deno))