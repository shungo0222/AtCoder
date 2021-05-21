def make_divisors(n):
    divisors = []
    i = 1
    while i*i <= n:
        tmp = []
        if n % i == 0:
            tmp.append(i)
            if i != n // i:
                tmp.append(n//i)
                divisors.append(tmp)
        i += 1
    return divisors

def main():
    n = int(input())
    divs = make_divisors(2*n)
    
    ans = 0
    for d in divs:
        if not (d[0] % 2) == (d[1] % 2):
            ans += 1
    print(2*ans)

if __name__ == '__main__':
    main()