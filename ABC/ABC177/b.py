import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = input()
    t = input()
    
    ans = 100000
    for i in range(len(s)-len(t)+1):
        tmp = s[i:i+len(t)]
        cnt = 0
        for j in range(len(t)):
            if t[j] != tmp[j]:
                cnt += 1
        ans = min(ans, cnt)
        
    print(ans)
    
if __name__ == '__main__':
    main()
