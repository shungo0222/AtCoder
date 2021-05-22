def main():
    s = input()
    ans = []
    for i in s:
        if i == '6':
            ans.append('9')
        elif i == '9':
            ans.append('6')
        else:
            ans.append(i)
    print(''.join(ans)[::-1])

if __name__ == '__main__':
    main()