def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    l = list(range(1, n+1))
    print('Yes' if a == l else 'No')

if __name__ == '__main__':
    main()