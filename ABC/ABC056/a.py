def main():
    a, b = input().split()
    if a == 'H':
        print(b)
    elif a == 'D' and b == 'H':
        print('D')
    elif a == 'D' and b == 'D':
        print('H')

if __name__ == '__main__':
    main()