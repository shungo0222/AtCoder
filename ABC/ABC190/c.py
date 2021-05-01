def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]

    ans = 0
    for i in range(2**k):
        slect = [0] * k
        for j in range(k):
            if (i >> j) & 1:
                slect[j] = 1
        
        plates = [0] * n
        for x, y in enumerate(slect):
            plates[cd[x][y]-1] += 1
        
        cnt = 0
        for a, b in ab:
            if plates[a-1] > 0 and plates[b-1] > 0:
                cnt += 1
        
        ans = max(ans, cnt)

    print(ans)

if __name__ == '__main__':
    main()