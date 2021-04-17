import sys
import math

def main():
    input = sys.stdin.readline
    a, b = map(int, input().split())

    ans = 0
    for i in range(1, b-a+1):
        x = math.ceil(a/i)
        if i*(x+1) <= b:
            ans = max(ans, i)

    print(ans)

if __name__ == '__main__':
    main()