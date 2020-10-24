import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1

    if 0 in a:
        print(0)
    else:
        for i in range(len(a)):
            ans *= a[i]
            if ans > (10**18):
                print(-1)
                sys.exit()
        else:
            print(ans)

if __name__ == '__main__':
    main()