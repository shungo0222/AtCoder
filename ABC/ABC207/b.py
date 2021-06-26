def main():
    a, b, c, d = map(int, input().split())
    if b >= c*d:
        print(-1)
    else:
        ans = 0
        blue, red = a, 0
        while True:
            if blue <= red*d:
                print(ans)
                exit()
            ans += 1
            blue += b
            red += c

if __name__ == '__main__':
    main()