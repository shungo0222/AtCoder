def main():
    a, b, c = map(int, input().split())
    mod = 10**9 + 7
    print((a*b%mod)*c%mod)

if __name__ == '__main__':
    main()