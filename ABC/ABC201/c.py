import itertools
import math

def main():
    s = input()
    
    sure = s.count('o')
    unsure = s.count('?')
    
    if sure > 4:
        print(0)
        exit()
    
    sure_n, unsure_n = [], []
    for i in range(10):
        if s[i] == 'o':
            sure_n.append(str(i))
        elif s[i] == '?':
            unsure_n.append(str(i))
    
    if sure == 4:
        print(24)
    else:
        ans = 0
        for i in itertools.combinations_with_replacement(sure_n+unsure_n, 4-sure):
            x = sure_n + list(i)
            y = 1
            for i in set(x):
                y *= math.factorial(x.count(i))
            ans += 24 // y
        print(ans)

if __name__ == '__main__':
    main()