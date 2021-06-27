def main():
    x = int(input())
    n = 1
    while True:
        if n**4 == x:
            print(n)
            exit()
        n += 1

if __name__ == '__main__':
    main()