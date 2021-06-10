import sys

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    print(min(m//2, (m-2*n)//4 + n))

if __name__ == '__main__':
    main()