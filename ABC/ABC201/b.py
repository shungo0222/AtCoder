def main():
    n = int(input())
    st = [list(input().split()) for _ in range(n)]
    st = sorted(st, key=lambda x: int(x[1]), reverse=True)
    print(st[1][0])

if __name__ == '__main__':
    main()