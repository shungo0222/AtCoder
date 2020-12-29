import math

n = int(input())
people = [int(input()) for _ in range(5)]
print(math.ceil(n/min(people))+4)