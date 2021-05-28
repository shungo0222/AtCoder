def main():
    a, b, c = map(int, input().split())
    for i in range(100):
        if (b * i + c) % a == 0:
            print('YES')
            exit()
    print('NO')

if __name__ == '__main__':
    main()