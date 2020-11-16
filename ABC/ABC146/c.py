a, b, x = map(int, input().split())
left = 0
right = 10**9 + 1
while right - left > 1:
    mid = (left + right) // 2
    if x < a*mid + b*(len(str(mid))):
        right = mid
    else:
        left = mid
print(left)