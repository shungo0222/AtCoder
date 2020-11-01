from collections import Counter

s = input()
c = Counter(list(s))

if len(s) <= 2:
    flag = False
    for i in range(1, 13):
        tmp = 8 * i
        if int(s) == tmp or int(s[::-1]) == tmp:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')
else:
    for i in range(13, 125):
        tmp = 8 * i
        c_tmp = Counter(list(str(tmp)))
        flag = True
        for key, val in c_tmp.items():
            if c[key] < val:
                flag = False
                break
        if flag:
            print('Yes')
            exit()
    print('No')