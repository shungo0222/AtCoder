import sys
input = sys.stdin.readline

def main():
    n = int(input())
    s = input()
    
    for i in range(n):
        if s[i] == '1':
            print('Takahashi' if i%2 == 0 else 'Aoki')
            exit()

if __name__ == '__main__':
    main()