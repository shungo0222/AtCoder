n, m = map(int, input().split())
penalty = dict()
penalty_cnt = 0
ans = set()
for _ in range(m):
    num, result = input().split()
    if result == 'AC':
        ans.add(num)
        if num not in penalty:
            penalty[num] = 0
    elif num not in ans:
        if num not in penalty:
            penalty[num] = 1
        else:
            penalty[num] += 1
ans = list(ans)
for i in range(len(ans)):
    penalty_cnt += penalty[ans[i]]
print(len(ans), penalty_cnt)