import sys

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    r = [[] for _ in range(n)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        r[a-1].append(b-1)
    
    for i in r[0]:
        for j in r[i]:
            if j == n-1:
                print('POSSIBLE')
                exit()
    
    print('IMPOSSIBLE')

if __name__ == '__main__':
    main()