import random

COUNT = 10
BASE = 1
TOP = 100

num=[0] * COUNT

for i in range(COUNT):
    num[i] = random.randint(BASE,TOP)

print("")

for i in num:
    print(i)