def main():
    n = int(input())
    x = int(1.08 * n)
    
    if x < 206:
        print('Yay!')
    elif x == 206:
        print('so-so')
    else:
        print(':(')

if __name__ == '__main__':
    main()