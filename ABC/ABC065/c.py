from math import factorial

def main():
    n, m = map(int, input().split())
    MOD = 10**9 + 7
    
    if m == n-1 or m == n+1:
        print(factorial(n)*factorial(m)%MOD)
    elif m == n:
        print(2*factorial(n)*factorial(m)%MOD)
    else:
        print(0)

if __name__ == '__main__':
    main()