import sys
input = sys.stdin.readline

from collections import defaultdict

def move(x, index, n):
    x_sorted = list(sorted(set(x)))
    x_new = [0] * n
    
    for i in range(len(x_sorted)):
        for j in index[x_sorted[i]]:
            x_new[j] = i+1
    
    return x_new

def main():
    h, w, n = map(int, input().split())
    a, b = [], []
    a_index = defaultdict(list)
    b_index = defaultdict(list)
    
    for k in range(n):
        i, j = map(int, input().split())
        a_index[i].append(k)
        b_index[j].append(k)
        a.append(i)
        b.append(j)
    
    a_new = move(a, a_index, n)
    b_new = move(b, b_index, n)
    
    for i in range(n):
        print(a_new[i], b_new[i])

if __name__ == '__main__':
    main()