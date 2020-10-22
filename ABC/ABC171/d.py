import sys
import collections
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    ans = [sum(a)]
    a = dict(collections.Counter(a))
    for i in range(q):
        b, c = map(int, input().split())
        if b in a.keys():
            ans.append(ans[i] + ((c - b) * a[b]))
            if c in a.keys():
                a[c] = a[b] + a[c]
            else:
                a[c] = a[b]
            del a[b]
        else:
            ans.append(ans[i])
    print(*ans[1:], sep='\n')

if __name__ == '__main__':
    main()