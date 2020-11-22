def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)

    divisors.sort()
    return divisors

s, p = map(int, input().split())
divs = make_divisors(p)
for i in range(len(divs) // 2):
    if (divs[i] + divs[len(divs) - i - 1]) == s:
        print('Yes')
        exit()
print('No')