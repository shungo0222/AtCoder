import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    print(a.index(b[-2])+1)

if __name__ == '__main__':
    main()