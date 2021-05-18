import numpy as np

def main():
    h, w = map(int, input().split())
    s = np.array([list(input()) for _ in range(h)])
    s = np.pad(s, (1, 2), 'constant', constant_values=('.'))
    
    for i in range(1, h+1):
        for j in range(1, w+1):
            if s[i][j] == '.':
                s[i][j] = np.sum(s[i-1:i+2, j-1:j+2] == '#')
    
    for i in range(1, h+1):
        print(''.join(s[i, 1:w+1]))

if __name__ == '__main__':
    main()