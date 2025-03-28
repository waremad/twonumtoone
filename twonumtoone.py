#[[A_MINorder,A_MIN,A_MAX],[B_MINorder,,A_MIN,B_MAX],[C_MINorder,,A_MIN,C_MAX]...]
import csv
import numpy as  np

n = [20,10]
ls = [[1,10,35],[1,5,17]]
def two2one(n,ls):
    ls_2 = []
    n_2 = []
    for i in range(len(n)):
        ls_2.append(int((10**ls[i][0])*(ls[i][2]-ls[i][1])))
        n_2.append(int((10**ls[i][0])*(n[i]-ls[i][1])))
    print("ls_2,n_2",ls_2,n_2)
    m = 1
    out = 0
    for i in range(len(n)):
        out += n_2[i]*m
        m = m * ls_2[i]
        print("out,m",out,m)
    return out

#"""
iris = []
with open("iris.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        iris.append(row)

for i in range(len(iris)-1):
    for j in range(4):
        iris[i+1][j] = float(iris[i+1][j])

patt = []
for i in range(4):
    minmax = []
    for j in iris[1:]:
        minmax.append(j[i])
    parsum = all(map(lambda x: str(x)[-2:] == ".0", minmax))
    nn = 0
    while not(parsum):
        #print("parsum,order,nn",parsum,order,nn)
        nn += 1
        parsum = all(map(lambda x: str(x*(10**nn))[-2:] == ".0", minmax))
        #print(order)
    patt.append([nn,min(minmax),max(minmax)])

print(patt)

#"""
iris_2 = []
for i in iris[1:]:
    iris_2.append([two2one(i[:-1],patt),i[-1]])

#print(iris_2)
#"""

iris_3 = sorted(iris_2)

#"""
for i in iris_3:
    print(",".join([str(i[0]),i[1]]))
#"""

befo = ""
out = []
out.append(iris_3[0])
for i in range(len(iris_3)):
    if i > 0:
        if iris_3[i][1] != befo:
            #print("?")
            for j in [1,0]:
                if not(iris_3[i - j] in out):
                    out.append(iris_3[i - j])
    befo = iris_3[i][1]

print()
for i in out:
    print(",".join([str(i[0]),i[1]]))