from math import comb
from collections import defaultdict

def main():
    n = int(input())
    
    d = defaultdict(int)
    for _ in range(n):
        s = input()
        if s[0] in 'MARCH':
            d[s[0]] += 1
    
    a = comb(sum(d.values()), 3)
    b = 0
    for i in d.keys():
        if d[i] >= 2:
            b += comb(d[i], 2) * (sum(d.values())-d[i])
        if d[i] >= 3:
            b += comb(d[i], 3)
    
    print(a-b)

if __name__ == '__main__':
    main()