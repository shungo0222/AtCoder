s = input()
if len(set(s)) == 2 and s.count(list(set(s))[0]) == 2 and s.count(list(set(s))[1]) == 2:
    print('Yes')
else:
    print('No')