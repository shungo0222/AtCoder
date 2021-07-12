import sys
input = sys.stdin.readline

def main():
    n = int(input())
    ans = float('inf')
    
    for i in range(1, int(n**0.5)+1):
        j = n//i
        ans = min(ans, abs(i-j) + (n-i*j))
    
    print(ans)

if __name__ == '__main__':
    main()