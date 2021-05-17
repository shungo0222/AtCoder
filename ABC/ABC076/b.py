def main():
    n = int(input())
    k = int(input())
    
    ans = 1
    for _ in range(n):
        if ans * 2 <= ans + k:
            ans *= 2
        else:
            ans += k
    print(ans)

if __name__ == '__main__':
    main()