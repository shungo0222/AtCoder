def main():
    s = input()
    print('YES' if s == s[::-1] else 'NO')

if __name__ == '__main__':
    main()