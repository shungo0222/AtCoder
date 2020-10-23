import sys
import collections
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    cnt_list = collections.Counter(a)
    search_list = [0] * (a[-1]+1)
    ans = 0
    for num, cnt in cnt_list.items():
        search_list[num] = cnt
    for i in a:
        if search_list[i] == 1:
            ans += 1
        for j in range(i, a[-1]+1, i):
            search_list[j] = 0
    print(ans)
    
if __name__ == '__main__':
    main()