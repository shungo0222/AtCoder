import sys
input = sys.stdin.readline

def main():
    x, y = map(int, input().split())
    print('Better' if x < y else 'Worse')

if __name__ == '__main__':
    main()