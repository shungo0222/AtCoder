import itertools

n = int(input())
p = tuple([int(i) for i in input().split()])
q = tuple([int(i) for i in input().split()])
seq = tuple(range(1, n+1))
num_p = 0
num_q = 0
cnt = 0
for i in itertools.permutations(seq):
    cnt += 1
    if i == p:
        num_p = cnt
    if i == q:
        num_q = cnt
print(abs(num_p-num_q))