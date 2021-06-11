import sys

class Cumsum2D(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.c = self._make_cumsum()
    
    def _make_cumsum(self):
        row, col = len(self.matrix), len(self.matrix[0])
    
        c = [[0]*(col+1) for _ in range(row+1)]
        for i in range(row):
            for j in range(col):
                c[i+1][j+1] = c[i][j+1] + c[i+1][j] - c[i][j] + self.matrix[i][j]

        return c
    
    def get_sum(self, row_index, col_index):
        return self.c[row_index[1]][col_index[1]] - self.c[row_index[1]][col_index[0]] \
                - self.c[row_index[0]][col_index[1]] + self.c[row_index[0]][col_index[0]]
    
    def show_cumsum(self):
        print('='*20)
        print('Cumsum')
        print('[', end='')
        print(*self.c, sep=',\n', end='')
        print(']')
        print('='*20)

def check(flag_list, n, k):
    c = Cumsum2D(flag_list)
    
    for i in range(k, n+1):
        for j in range(k, n+1):
            if c.get_sum([i-k, i], [j-k, j]) < k**2 // 2 + 1:
                return True
    return False

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    
    ok, ng = 10**10, -1
    while ok != ng+1:
        mid = (ok + ng) // 2
        
        tmp = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if a[i][j] > mid:
                    tmp[i][j] = 1
        
        if check(tmp, n, k):
            ok = mid
        else:
            ng = mid
    
    print(ok)

if __name__ == '__main__':
    main()