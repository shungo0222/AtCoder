def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

n, k = map(int, input().split())
num = len(list(Base_10_to_n(n, k)))
print(num)