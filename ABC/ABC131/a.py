import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = input()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            print('Bad')
            return
    print('Good')
    
if __name__ == '__main__':
    main()