import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    add = 1
    if x not in p:
        print(x)
    else:
        while True:
            if (x - add) not in p:
                print(x - add)
                return
            elif (x + add) not in p:
                print(x + add)
                return
            else:
                add += 1

if __name__ == '__main__':
    main()