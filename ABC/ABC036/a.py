import sys
import math
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    print(math.ceil(b/a))

if __name__ == '__main__':
    main()