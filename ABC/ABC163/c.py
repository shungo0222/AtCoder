import collections
n = int(input())
a = [int(i) for i in input().split()]
cnt = collections.Counter(a)

for i in range(1, n+1):
    print(cnt[i])