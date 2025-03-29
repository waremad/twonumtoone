import numpy as  np
import random

a = np.array(["1","2","3"])

xs = [1,2,3]

print(sum(list(map(lambda x: x%1, xs))))

if 0.1:
    print(True)

if not(0):
    print(False)

a = [1,2]
b = [3,4]
print(a+b)

def floatset():
    pass

for i in range(10):
    n = random.randint(1,9999)/100
    print(n,str(n*10**2),n*10**2%1)

