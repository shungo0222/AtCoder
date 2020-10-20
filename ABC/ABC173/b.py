import sys
import collections
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s = collections.Counter(s)
    print('AC x {}'.format(s['AC']))
    print('WA x {}'.format(s['WA']))
    print('TLE x {}'.format(s['TLE']))
    print('RE x {}'.format(s['RE']))
    
if __name__ == '__main__':
    main()