n = input()

if n == '0':
    print('Yes')
else:
    for i in range(len(n)-1, -1, -1):
        if n[i] != '0':
            x = n[:i+1]
            break

    for i in range(len(x)//2):
        if x[i] != x[len(x)-1-i]:
            print('No')
            exit()
    
    print('Yes')