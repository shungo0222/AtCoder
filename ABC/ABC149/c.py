x = int(input())
if x == 2:
    print(x)
else:
    while True:
        for i in range(2, x):
            if x % i == 0:
                break
            if i == x-1:
                print(x)
                exit()
        x += 1