import numpy as np
import csv
import matplotlib.pyplot as plt
import cvxpy
from cvxpy import *

# dimension of each point
d = 2
# number of x elements of one type
m = 0 
# number of elements of other type
n = 0  

finput = "Xsvm.csv"
foutput = "ysvm.csv" 

z=list()

# generate x points
# generate y points

with open(foutput,'r') as csvfile :

    csvreader = csv.reader(csvfile)

    for row in csvreader :
        for elements in row : 
            z.append(float(elements))

# created a list and finally written +1's and -1's

with open(finput,'r') as csvfile :

    csvreader = csv.reader(csvfile)

    k = 0
    for row in csvreader : 
        temp = list() 
        if(z[k]>0) : 
            # this belongs to x
            for elements in row :
                temp.append(elements)
            if(m==0):
                x=np.array([temp])
            else :
                x=np.vstack((x,temp))
            m = m+1
        else :
            # this belongs to y
            for elements in row :
                temp.append(elements) 
            if(n==0):
                y = np.array([temp])
            else :
                y=np.vstack((y,temp))
            n = n+1
        k=k+1        

p=np.empty((m,2))
q=np.empty((n,2))

for i in range(0,m):
    p[i]=x[i,:]
for i in range(0,n):
    q[i]=y[i,:]

# print(x[0,:])

a = Variable(d)
b = Variable()
t = Variable()

obj = Maximize(t)

x_constraints = [a.T * p[i] - b >= t  for i in range(m)]
y_constraints = [a.T * q[i] - b <= -t for i in range(n)]

constraints = x_constraints +  y_constraints + [norm(a,2) <= 1]

prob = Problem(obj, constraints)
prob.solve() 

a0 =a[0].value
a1 = a[1].value
B = b.value
T = t.value

# print(a.value,b.value,t.value)

# if for a point x,  a.T*(x) - b >=t then it belongs to class 1
# else if a.T*x-b <t then it belongs to class -1

inp=[[2,0.5],[0.8,0.7],[1.58,1.33],[0.08,0.001]]

for i in range(0,len(inp)):
    calc = a0*inp[i][0]+a1*inp[i][1]-B    
    if(calc>=T):
        print(i,"Class 1")
    else :
        print(i,"Class -1")