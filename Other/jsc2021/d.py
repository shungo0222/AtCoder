def main():
    MOD = 10 ** 9 + 7
    n, p = map(int, input().split())
    ans = (p - 1) * pow(p - 2, n - 1, MOD) % MOD
    print(ans)

if __name__ == '__main__':
    main()