def main():
    n = int(input())
    
    tlr = []
    for _ in range(n):
        t, l, r = map(float, input().split())
        if t == 1:
            tlr.append([l, r])
        elif t == 2:
            tlr.append([l, r-0.01])
        elif t == 3:
            tlr.append([l+0.01, r])
        elif t == 4:
            tlr.append([l+0.01, r-0.01])
    
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            l_i, r_i = tlr[i]
            l_j, r_j = tlr[j]
            if (l_j <= l_i <= r_j) or (l_j <= r_i <= r_j) or (l_i <= l_j and r_i >= r_j):
                ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()