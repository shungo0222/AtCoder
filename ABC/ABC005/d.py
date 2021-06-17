class Cumsum2D(object):
    """
    2 dim cumsum
    
    Parameters
    ----------
    matrix : list
        the original matrix
    c : list
        the cumsum of matrix
    """
    
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

def main():
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(n)]
    d = Cumsum2D(d)
    
    comb = [[i, j] for i in range(1, n+1) for j in range(1, n+1)]
    yummy = []
    for i, j in comb:
        tmp = 0
        for k in range(n-i+1):
            for l in range(n-j+1):
                tmp = max(tmp, d.get_sum([k, k+i], [l, l+j]))
        yummy.append(tmp)
    
    q = int(input())
    for _ in range(q):
        p = int(input())
        
        ans = 0
        for i, (x, y) in enumerate(comb):
            if x*y <= p:
                ans = max(ans, yummy[i])

        print(ans)

if __name__ == '__main__':
    main()