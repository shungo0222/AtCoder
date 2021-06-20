from collections import Counter, defaultdict

def main():
    n = int(input())
    s = input()
    c = Counter(s)
    d = defaultdict(int)
    
    ans = float('inf')
    for i in range(n):
        if s[i] == 'E':
            ans = min(ans, c['E'] - d['E'] - 1 + d['W']) 
        else:
            ans = min(ans, c['E'] - d['E'] + d['W'])
        d[s[i]] += 1
    print(ans)

if __name__ == '__main__':
    main()