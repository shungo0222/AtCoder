import sys
input = sys.stdin.readline

def main():
    n = int(input())
    c = list(map(int, input().split()))
    MOD = 10**9 + 7
    
    ans = 1
    x = 0
    for i in sorted(c):
        ans = (ans * (i-x)) % MOD
        x += 1
    print(ans%MOD)

if __name__ == '__main__':
    main()