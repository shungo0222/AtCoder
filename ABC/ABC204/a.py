def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    else:
        for i in [0, 1, 2]:
            if x != i and y != i:
                print(i)

if __name__ == '__main__':
    main()