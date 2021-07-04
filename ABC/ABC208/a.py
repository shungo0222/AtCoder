def main():
    a, b = map(int, input().split())
    print('No' if a*6 < b or a > b else 'Yes')

if __name__ == '__main__':
    main()