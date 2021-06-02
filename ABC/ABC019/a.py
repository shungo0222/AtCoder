import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    age = sorted(list(map(int, input().split())))
    print(age[1])
            
if __name__ == '__main__':
    main()