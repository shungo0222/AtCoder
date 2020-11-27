n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
print(a[0] + 2 * sum(a[1:n//2]) + (a[n//2] if n % 2 == 1 else 0))