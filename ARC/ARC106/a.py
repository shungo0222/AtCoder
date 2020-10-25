def main():
    n = int(input())

    i = 1
    while n >= 5 ** i:
        tmp = n - (5 ** i)
        j = 1
        while tmp >= 3 ** j:
            if tmp == 3 ** j:
                print(j, i)
                return
            else:
                j += 1
        i += 1
    print(-1)
        
if __name__ == '__main__':
    main()