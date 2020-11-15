ab = [int(input()) for _ in range(2)]
for i in range(1,4):
    if i not in ab:
        print(i)
        exit()