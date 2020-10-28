import sys
K = int(input())
A, B = map(int, input().split())

i = 1
while(True):
    if((A<=K*i) and (K*i<=B)):
        print('OK')
        sys.exit()
    if(B<K*i):
        print('NG')
        sys.exit()
    i += 1