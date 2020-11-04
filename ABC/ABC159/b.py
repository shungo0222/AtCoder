import sys
s = list(input())
front, back = list(), list()

repeat = (len(s)-1) // 2
for i in range(repeat):
    if s[i] == s[len(s)-1-i]:
        front.append(s[i])
        back.append(s[len(s)-1-i])
    else:
        print('No')
        sys.exit()

if len(front) % 2 == 0:
    repeat = len(front) // 2
else:
    repeat = (len(front)-1) // 2        

for i in range(repeat):
    if front[i] == front[len(front)-1-i] and back[i] == back[len(back)-1-i]:
        pass
    else:
        print('No')
        sys.exit()
        
print('Yes')