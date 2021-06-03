def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a + [0]
    
    s = 0
    for i in range(len(a) - 1):
        s += abs(a[i] - a[i + 1])
    
    for i in range(len(a) - 2):
        print(s - (abs(a[i] - a[i + 1]) + abs(a[i + 1] - a[i + 2])) + abs(a[i] - a[i + 2]))

if __name__ == '__main__':
    main()