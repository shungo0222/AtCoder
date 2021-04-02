import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    a = list(map(int, input().split()))

    ans = float('inf')
    for i in range(2 ** (n-1)):
        div = bin(i)[2:].zfill(n-1)
        or_ = a[0]
        xor = 0
        for j in range(n-1):
            if div[j] == '0':
                or_ |= a[j+1]
            else:
                xor ^= or_
                or_ = a[j+1]
        xor ^= or_
        ans = min(ans, xor)

    print(ans)

if __name__ == '__main__':
    main()