import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    h = (60 * (n % 12) + m) * 0.5
    m = m * 6
    print(min(abs(h-m), 360-abs(h-m)))
            
if __name__ == '__main__':
    main()