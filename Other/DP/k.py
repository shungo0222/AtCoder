def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    dp = [False for _ in range(200005)]
    
    for i in range(k):
        for j in range(n):
            if not dp[i]:
                dp[i+a[j]] = True
    
    print('First' if dp[k] else 'Second')

if __name__ == '__main__':
    main()