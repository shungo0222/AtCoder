def main():
    n, m = map(int, input().split())
    students_coor = [list(map(int, input().split())) for _ in range(n)]
    checkpoints_coor = [list(map(int, input().split())) for _ in range(m)]
    
    ans = []
    for i in range(n):
        a, b = students_coor[i]
        dis = float('inf')
        point = 0
        for j in range(m):
            c, d = checkpoints_coor[j]
            if abs(a - c) + abs(b - d) < dis:
                dis = abs(a - c) + abs(b - d)
                point = j + 1
        ans.append(point)
    
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()