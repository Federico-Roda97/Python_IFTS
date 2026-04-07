import random
# from random import *

N = 5

e = []

n = 0

while n < N:
    x = random.randint(1,90)
    if x in e:
        pass
    else:
        e.append(x)
        n += 1

print(e)