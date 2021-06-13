from collections import Counter

def binary_search(key, target_list):
    left = 0
    right = len(target_list)
    while left < right:
        mid = (left + right) // 2
        if target_list[mid] == key:
            return target_list[mid-1]
        elif key < target_list[mid]:
            right = mid
        else:
            left = mid + 1
    return target_list[left-1]

def main():
    n, q = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    
    x = [0]
    y = {0: 0}
    for i in range(len(a)-1):
        t = a[i+1] - a[i] - 1 + x[i]
        x.append(t)
        if t not in y:
            y[t] = a[i+1]
    
    c = Counter(x)
    l = sorted(list(c.keys()))
    
    for q in k:
        if q > l[-1]:
            print(y[l[-1]] + c[l[-1]] - 1 + q - l[-1])
        else:
            b = binary_search(q, l)
            print(y[b] + c[b] - 1 + q - b)

if __name__ == '__main__':
    main()