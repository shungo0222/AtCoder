import sys
import collections

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    cnt_list = collections.Counter(s)
    print(len(cnt_list.keys()))

if __name__ == '__main__':
    main()