def main():
    s = [input() for _ in range(3)]
    index = [0] * 3
    length = [len(i) for i in s]
    x = 'a'
    
    while True:
        i = ord(x) - ord('a')
        if index[i] < length[i]:
            x = s[i][index[i]]
            index[i] += 1
        else:
            print(x.upper())
            exit()

if __name__ == '__main__':
    main()