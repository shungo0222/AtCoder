import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    a = list(map(int, input().split()))
    
    print(n * sum([i*i for i in a]) - (sum(a)) ** 2)

if __name__ == '__main__':
    main()