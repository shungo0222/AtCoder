import sys

def main():
    a, b = input().split()
    a = int(a)
    b = int(b.replace('.',''))
    print(a*b//100)

if __name__ == '__main__':
    main()


# import sys
# from decimal import Decimal

# def main():
#     a, b = input().split()
#     print(int(Decimal(a)*Decimal(b)))

# if __name__ == '__main__':
#     main()