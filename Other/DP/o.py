# bitDP

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    MOD = 10**9 + 7
    
    # dp[s] := それぞれの男たちが、集合sで示される女たちとペアになるパターン数
    dp = [0]*(1<<n)
    
    # 初期化
    dp[0] = 1
    
    # iからi+1の遷移の際、考慮する集合
    xs = {0}
    
    # 一人ずつ男を読み込み計算する
    for i in range(n):
        a = list(map(int, input().split()))
        
        # 好相性の人のビットフラグ
        flags = [1 << i for i, j in enumerate(a) if j == 1]
        
        # 次の遷移の際に考慮する集合
        next_xs = set()
        
        for x in xs:
            # パターン数
            pat_cnt = dp[x] % MOD
            
            for f in flags:
                # すでに特定の女が他の男とペアになっているので何もしない
                if x & f:
                    continue
                
                # ペアが1組作れるので、加算する
                dp[x | f] += pat_cnt
                next_xs.add(x | f)
        
        xs = next_xs
    
    print(dp[-1]%MOD)

if __name__ == '__main__':
    main()