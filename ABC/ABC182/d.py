from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

cumsum = list(accumulate(a))
max_list = [cumsum[0]] * n
for i in range(1, n):
    max_list[i] = max(cumsum[i], max_list[i - 1])

coor = 0
max_coor = 0

for i in range(n):
    max_coor = max(max_coor, coor + max_list[i])
    coor += cumsum[i]

print(max_coor)