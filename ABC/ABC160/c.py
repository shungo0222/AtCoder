k, n = list(map(int, input().split()))
a = list(map(int, input().split()))

i = 0
length = []
while(i < n):
    if(i == (n-1)):
        length.append(abs((k-a[i]) + a[0]))
    else:
        length.append(abs(a[i+1]-a[i]))
    i += 1

length_sort = sorted(length)
min = sum(length_sort[:n-1])

print(min)