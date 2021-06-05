def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    cnt = [0] * 9
    for i in a:
        if i // 400 >= 8:
            cnt[8] += 1
        else:
            cnt[i // 400] += 1
    
    min_ = 8 - cnt[:8].count(0)
    max_ = min_ + cnt[8]
    
    print(max(1, min_), max_)

if __name__ == '__main__':
    main()