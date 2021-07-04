def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    b = []
    for i, j in enumerate(a):
        b.append([j, i, k//n])
    b = sorted(b)
    
    for i in range(k%n):
        b[i][2] += 1
    
    b = sorted(b, key=lambda x: x[1])
    
    for i in b:
        print(i[2])

if __name__ == '__main__':
    main()