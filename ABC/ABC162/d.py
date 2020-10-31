import collections
n = int(input())
s = [''] + list(input())
cnt_1 = collections.Counter(s)

sub = 0
for j in range(1, (n+1)//2):
    for i in range(1, n-2*j+1):
        tmp = s[i] + s[i+j] + s[i+j*2]
        cnt_2 = collections.Counter(tmp)
        if max(cnt_2.values()) == 1:
            sub += 1

print((cnt_1['R']*cnt_1['G']*cnt_1['B'])-sub)