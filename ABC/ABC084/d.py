import numpy as np

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

def main():
    primes = get_sieve_of_eratosthenes(100000)
    
    a = np.array([0] * 100001)
    a[primes] = 1
    
    b = np.array([0] * 100001)
    for i in primes[1:]:
        if a[(i+1)//2] == 1:
            b[i] = 1
    
    c = np.cumsum(b)
    
    q = int(input())
    
    for _ in range(q):
        l, r = map(int, input().split())
        print(c[r]-c[l-1])

if __name__ == '__main__':
    main()