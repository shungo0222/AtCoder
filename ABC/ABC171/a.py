import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    if input().isupper():
        print('A')
    else:
        print('a')

if __name__ == '__main__':
    main()