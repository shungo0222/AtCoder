n = int(input())
b = [i for i in range(1,10)]
for a in range(1,10):
    if n % a == 0 and n // a in b:
        print('Yes')
        exit()
print('No')