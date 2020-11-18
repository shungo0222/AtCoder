import itertools
import math

n = int(input())
loc = [list(map(int,input().split())) for _ in range(n)]
arr = list(itertools.permutations(loc))
p = math.factorial(n)
dis = 0
for i in range(p):
    for j in range(n-1):
        dis += math.sqrt((arr[i][j+1][1]-arr[i][j][1])**2+(arr[i][j+1][0]-arr[i][j][0])**2)
print(dis/p)