h = int(input())
attack = 0
cnt = 0
while h >= 2:
    h //= 2
    cnt += 1
for i in range(cnt+1):
    attack += 2 ** i          
print(attack)