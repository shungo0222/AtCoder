from math import factorial

def main():
    p = int(input())
    
    ans = 0
    for i in [factorial(i) for i in range(10, 0, -1)]:
        x = p // i
        y = p % i
        ans += x
        p = y
    
    print(ans)

if __name__ == '__main__':
    main()