import sys
input = sys.stdin.readline

def main():
    n = int(input())
    s = [list(input().strip()) for _ in range(n)]
    
    ans = [['']*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            ans[j][n-i-1] = s[i][j]
    
    for i in ans:
        print(''.join(i))

if __name__ == '__main__':
    main()