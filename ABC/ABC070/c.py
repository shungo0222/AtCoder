import math
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    t = set([int(input()) for _ in range(n)])
    
    lcm = lambda a, b: a*b // math.gcd(a, b)
    
    ans = 1
    for i in t:
        ans = lcm(ans, i)
    
    print(ans)

if __name__ == '__main__':
    main()