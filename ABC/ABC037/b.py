import sys
input = sys.stdin.readline

def main():
    n, q = map(int, input().split())
    ans = [0] * n
    
    for _ in range(q):
        l, r, t = map(int, input().split())
        
        for i in range(l-1, r):
            ans[i] = t
    
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()