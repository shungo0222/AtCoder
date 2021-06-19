def main():
    n = int(input())
    
    s = 0
    i = 1
    while True:
        s += i
        if s >= n:
            print(i)
            exit()
        i += 1

if __name__ == '__main__':
    main()