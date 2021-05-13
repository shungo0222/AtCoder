def main():
    x, y, z = map(int, input().split())
    ans = 0
    while (y*ans + (ans+1)*z) <= x:
        ans += 1
    
    print(ans-1)

if __name__ == '__main__':
    main()