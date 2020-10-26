n, k = map(int, input().split())
i = 0
children = set()
while(i < k):
    input()
    children = children | set(map(int, input().split()))
    i += 1
print(n - len(children))