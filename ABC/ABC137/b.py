k, x = map(int, input().split())
black = [i for i in range(x-(k-1), x+k)]
print(*black)