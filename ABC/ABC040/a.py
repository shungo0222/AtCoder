import sys

def main():
    input = sys.stdin.readline
    
    n, x = map(int, input().split())
    print(min(abs(x-1), abs(n-x)))

if __name__ == '__main__':
    main()