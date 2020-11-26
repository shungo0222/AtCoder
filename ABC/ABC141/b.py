s = list(input())
for i in range(len(s)):
    if s[i] == 'U' or s[i] == 'D':
        pass
    elif i % 2 == 0 and s[i] == 'R':
        pass
    elif i % 2 == 1 and s[i] == 'L':
        pass
    else:
        print('No')
        exit()
print('Yes')