import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    time = 1900*m + 100*(n-m)
    print(time*2**m)

if __name__ == '__main__':
    main()