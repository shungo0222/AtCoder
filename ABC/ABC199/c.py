def main():
    n = int(input())
    s = input()
    q = int(input())
    t = [list(map(int, input().split())) for _ in range(q)]
    
    idx = list(range(2*n))
    two = 0
    
    for i in range(q):
        if t[i][0] == 1:
            if two % 2 == 1:
                for j in range(1, 3):
                    if t[i][j] < n+1:
                        t[i][j] += n
                    else:
                        t[i][j] -= n
            tmp = idx[t[i][1]-1]
            idx[t[i][1]-1] = idx[t[i][2]-1]
            idx[t[i][2]-1] = tmp
        else:
            two += 1

    if two % 2 == 1:
        idx = idx[n:] + idx[:n]
    
    for i in idx:
        print(s[i], end='')
    print()

if __name__ == '__main__':
    main()