import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    p = sorted(list(map(int, input().split())))
    print(sum(p[:k]))


if __name__ == '__main__':
    main()