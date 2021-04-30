import math

def main():
    n = int(input())
    cnt = set()
    x = int(math.sqrt(n))
    for i in range(2, x+1):
        j = i * i
        while j <= n:
            cnt.add(j)
            j *= i
    print(n - len(cnt))

if __name__ == '__main__':
    main()