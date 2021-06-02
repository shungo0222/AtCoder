import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = input() + ' '
    ans = []
    cnt = 1
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            ans.append(s[i]+str(cnt))
            cnt = 1
    print(''.join(ans))
            
if __name__ == '__main__':
    main()