import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    ans = ''
    for i in range(1, 20):
        if n <= 26**i:
            n -= 1
            for j in range(i):
                ans += chr((n % 26) + ord('a'))
                n //= 26
            print(ans[::-1])
            return
        else:
            n -= 26**i

if __name__ == '__main__':
    main()