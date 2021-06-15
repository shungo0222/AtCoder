import bisect

def main():
    n, q = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    
    x = [0]
    for i in range(len(a)-1):
        x.append(a[i+1]-a[i]-1+x[i])
    
    for _ in range(q):
        k = int(input())
        i = bisect.bisect_left(x, k)
        if i == 1:
            print(k)
        elif i == len(x):
            print(k-x[-1]+a[-1])
        else:
            print(k-x[i-1]+a[i-1])

if __name__ == '__main__':
    main()