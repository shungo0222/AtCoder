import sys
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    for i in range(256):
        if a ^ i == b:
            print(i)
            exit()

if __name__ == '__main__':
    main()