def main():
    w, a, b = map(int, input().split())
    
    if (a <= b <= a + w) or (a <= b + w <= a + w):
        print(0)
    elif a + w < b:
        print(b - (a + w))
    else:
        print(a - (b + w))

if __name__ == '__main__':
    main()