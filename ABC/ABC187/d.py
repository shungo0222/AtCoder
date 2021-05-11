def main():
    n = int(input())
    diffs = []
    a_max = 0
    for _ in range(n):
        a, b = map(int, input().split())
        diffs.append(2 * a + b)
        a_max -= a
    
    diffs.sort(reverse=True)
    ans = 0
    for diff in diffs:
        a_max += diff
        ans += 1
        if a_max > 0:
            break
    print(ans)

if __name__ == '__main__':
    main()