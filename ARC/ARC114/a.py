import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    x = list(map(int, input().split()))
    
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    ans = float('inf')
    
    for i in range(2 ** 15):
        tmp = 1
        for j in range(15):
            if (i >> j) & 1:
                tmp *= primes[j]
        
        if tmp != 1:
            for k in x:
                ok = False
                for l in range(2, k+1):
                    if (tmp % l == 0) and (k % l == 0):
                        ok = True
                        break
                
                if not ok:
                    break
            
            if ok:
                ans = min(ans, tmp)

    print(ans)

if __name__ == '__main__':
    main()