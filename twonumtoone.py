#[[A_MINorder,A_MIN,A_MAX],[B_MINorder,,A_MIN,B_MAX],[C_MINorder,,A_MIN,C_MAX]...]
import csv
import numpy as  np

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

def allprint(ls):
    for i in ls:
        print(i)

#"""""
iris = []
outline = 0#出力がある列
labelrow = [0]#データではないラベルなどの行
nonnum = [2,3,7,9,10]#数字ではない列
with open("titanic.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        iris.append(row)

iris_1_2 = []
for i in range(len(iris)):
    if not(i in labelrow):
        if outline in [0,-1,len(iris[0])]:
            if outline == 0:
                iris_1_2.append(iris[i][1:]+[iris[i][0]])
            else:
                #print("i,iris",i,iris)
                iris_1_2.append(iris[i][:-1]+[iris[i][-1]])
        else:
            #print(iris[i][:outline],iris[i][outline+1:],[iris[i][outline]])
            iris_1_2.append(iris[i][:outline]+iris[i][outline+1:]+[iris[i][outline]])

#allprint(iris_1_2)

nonnum_2 = nonnum[:]
nonnum = []
for i in nonnum_2:
    if outline < i:
        nonnum.append(i-1)
    else:
        nonnum.append(i)

for i in nonnum:
    memolabel = []
    iris_1_15 = iris_1_2[:]
    iris_1_2 = []
    for j in iris_1_15:
        #print("j,i",j,i)
        memo = j
        if memo[i] in memolabel:
            pass
        else:
            memolabel.append(memo[i])
        memo[i] = memolabel.index(memo[i])
        iris_1_2.append(memo)
    #print(memolabel)

#allprint(iris_1_2)

#for i in range(len(iris)-1):
#    for j in range(4):
#        iris[i+1][j] = float(iris[i+1][j])

iris = []
for i in iris_1_2:
    now = []
    for j in i:
        if j == "":
            now.append(0)
        else:
            now.append(float(j))
    iris.append(now)
wide = len(iris_1_2[0]) - 1

print(0)

patt = []
for i in range(wide):
    minmax = []
    for j in iris:
        minmax.append(j[i])
    parsum = all(map(lambda x: str(x)[-2:] == ".0", minmax))
    nn = 0
    print(1)
    print("minmax",minmax)
    while not(parsum):
        print("parsum,nn",parsum,nn,str(minmax[0]*(10**nn))[-2:],type(minmax[0]*(10**nn)))
        nn += 1
        parsum = all(map(lambda x: str(x*(10**nn))[-2:] == ".0", minmax))
        #print(order)
    patt.append([nn,min(minmax),max(minmax)])

print(patt)

#""""""
iris_2 = []
for i in iris:
    iris_2.append([two2one(i,patt),i[-1]])

#print(iris_2)
#""""""

iris_3 = sorted(iris_2)

"""
for i in iris_3:
    print(",".join([str(i[0]),i[1]]))
"""

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
#"""