import sys
input = sys.stdin.readline

def main():
    n = int(input())
    if n%2 == 0:
        print(n-1)
    else:
        print(n+1)

if __name__ == '__main__':
    main()