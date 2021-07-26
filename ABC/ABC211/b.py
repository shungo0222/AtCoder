import sys
input = sys.stdin.readline

def main():
    s = set([input().strip() for _ in range(4)])
    print('Yes' if len(s)==4 else 'No')

if __name__ == '__main__':
    main()