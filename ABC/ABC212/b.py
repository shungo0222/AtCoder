import sys
input = sys.stdin.readline

def main():
    x = list(input().rstrip())

    if len(set(x)) == 1:
        print('Weak')
        exit()
    
    x = ''.join(x)

    s = '0123456789012'
    for i in range(10):
        if s[i:i+4] == x:
            print('Weak')
            exit()
    
    print('Strong')

if __name__ == '__main__':
    main()