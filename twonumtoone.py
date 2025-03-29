#[[A_MINorder,A_MIN,A_MAX],[B_MINorder,,A_MIN,B_MAX],[C_MINorder,,A_MIN,C_MAX]...]
import csv
import numpy as  np

def two2one(n,ls):#オーダー、最大最小値を考慮して複数のデータを一つの値に変換する
    ls_2 = []
    n_2 = []
    for i in range(len(n)):
        ls_2.append(int((10**ls[i][0])*(ls[i][2]-ls[i][1])))
        n_2.append(int((10**ls[i][0])*(n[i]-ls[i][1])))
    #print("ls_2,n_2",ls_2,n_2)
    m = 1
    out = 0
    for i in range(len(n)):
        out += n_2[i]*m
        m = m * ls_2[i]
        #print("out,m",out,m)
    return out

def allprint(ls):#リストの中身を順に出力
    for i in ls:
        print(i)

def pointposi(cha):#小数点の位置から整数にするための桁
    if not("." in cha):
        return 0
    return len(cha) - cha.find(".") - 1

"""
-1
1. 2-1=1
1.2 3-1=2
0.34 4-1=3
"""

#"""""

#ファイルからリストヘ
iris = []
outline = 0#出力がある列
labelrow = [0]#データではないラベルなどの行
nonnum = [2,3,7,9,10]#数字ではない列
with open("titanic.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        iris.append(row)

#出力の列を-1にする
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

#outlineを考慮してnonnumをずらす
nonnum_2 = nonnum[:]
nonnum = []
for i in nonnum_2:
    if outline < i:
        nonnum.append(i-1)
    else:
        nonnum.append(i)

#数字ではない列に数字を割り当てる
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

#floatに変換
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

#strに変換
iris_str = []
for i in iris_1_2:
    now = []
    for j in i:
        if j == "":
            now.append("0")
        else:
            now.append(str(j))
    iris_str.append(now)

print(0)

patt = []
for i in range(wide):
    minmax = []
    minmax_str = []
    for j in iris:
        minmax.append(j[i])
    for j in iris_str:
        minmax_str.append(j[i])

    nn = max(list(map(pointposi, minmax_str)))

    patt.append([nn,min(minmax),max(minmax)])

print("patt",patt)

#""""""
iris_2 = []
for i in iris:
    iris_2.append([two2one(i[:-1],patt),i[-1]])

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

#print(out)
for i in out:
    print(str(i[1]) + "," + str(i[0]))
    #pass
#"""