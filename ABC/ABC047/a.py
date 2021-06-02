def main():
    abc = sorted(list(map(int, input().split())))
    if abc[0] + abc[1] == abc[2]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()