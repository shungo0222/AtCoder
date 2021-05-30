def main():
    n, k = map(int, input().split())
    ab = sorted([list(map(int, input().split())) for _ in range(n)])
    
    location = 0
    money = k
    for a, b in ab:
        if location == a:
            money += b
        elif (a - location) <= money:
            money = money - (a - location) + b
            location += (a - location)
        else:
            location += money
            money = 0
            break
    
    location += money
    location = min(location, 10**100)
    print(location)

if __name__ == '__main__':
    main()