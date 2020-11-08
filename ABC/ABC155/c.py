import collections

n = int(input())
s = [input() for _ in range(n)]
cnt = collections.Counter(s)
cnt_max = max(cnt.values())
d = [k for k, v in cnt.items() if v == cnt_max]
d = sorted(d)
print(*d, sep='\n')