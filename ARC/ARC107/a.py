MOD = 998244353

a, b, c = map(int, input().split())
A = a * (a + 1) // 2
B = b * (b + 1) // 2
C = c * (c + 1) // 2

tmp = B * C % MOD
print(tmp * A % MOD)