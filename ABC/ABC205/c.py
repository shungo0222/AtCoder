def check(a, b):
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')

def main():
    a, b, c = map(int, input().split())
    
    if a >= 0 and b >= 0:
        check(a, b)
    elif a < 0 and b >= 0:
        if c % 2 == 0:
            a *= -1
            check(a, b)
        else:
            print('<')
    elif a >= 0 and b < 0:
        if c % 2 == 0:
            b *= -1
            check(a, b)
        else:
            print('>')
    elif a < 0 and b < 0:
        if c % 2 == 0:
            a *= -1
            b *= -1
        check(a, b)

if __name__ == '__main__':
    main()