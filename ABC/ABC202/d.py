from math import factorial

def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def main():
    a, b, k = map(int, input().split())
    
    a_left = a
    b_left = b
    ans = []
    
    while a_left > 0 and b_left > 0:
        tmp = comb(a_left-1+b_left, a_left-1)
        if k <= tmp:
            ans.append('a')
            a_left -= 1
        else:
            ans.append('b')
            b_left -= 1
            k -= tmp
    
    ans.append('a' * a_left)
    ans.append('b' * b_left)
    
    print(''.join(ans))

if __name__ == '__main__':
    main()