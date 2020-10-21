import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    S = list(input())
    T = list(input())
    ans = 0
    for s, t in zip(S, T):
        if s != t:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()