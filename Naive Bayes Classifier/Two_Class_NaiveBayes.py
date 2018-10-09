# python3 programming_1.py
import csv
import numpy as np
import math

finput = "X.csv"
foutput = "Y.csv"

x1 = []
x2 = []
y= []
Data = []
x00 = []
x01 = []
x10 = []
x11 = []
test=[[1,1],[1,-1],[-1,1],[-1,-1]]

# calculation of mean
def mean(inp):
	Sum= 0.00
	for i in inp:
		Sum = Sum + float(i)
	Mean = (Sum/len(inp))
	return Mean

# calculation of variance
def variance(inp):
	Mean = mean(inp)
	Sum = 0.00
	for i in inp :
		Sum = Sum + (float(i) -Mean)*(float(i)-Mean)
	Variance = (Sum/len(inp))
	return Variance				

# normal distribution calculation
def normal(xinp,minp,vinp) :
	pr = (np.exp(-(xinp-minp)*(xinp-minp)/ (2*(vinp))))
	pr = pr / (math.sqrt(vinp*2*np.pi))
	return pr

# multiplying probabilities of probabilities of particular y
def probability(inp1,inp2):
	pr1 = normal(inp1[0],inp1[1],inp1[2])
	pr2 = normal(inp2[0],inp2[1],inp2[2])
	return (pr1*pr2)

with open(finput,'r') as csvfile :

	csvreader = csv.reader(csvfile)

	i = 0 
	for row in csvreader : 
		for elements in row :
			if(i==0) :  
				x1.append(float(elements))
			else :
				x2.append(float(elements))		
		i = i + 1		

with open(foutput,'r') as csvfile :

	csvreader = csv.reader(csvfile)

	for row in csvreader :
		for elements in row : 
	 		y.append(float(elements))	 	

for k in range(0,1000):		
	if(y[k]>0) :
		x00.append(x1[k])
		x10.append(x2[k])
	else :
		x01.append(x1[k])
		x11.append(x2[k])

# calculating mean and variance for different j,k
m00=mean(x00)
v00=variance(x00)
m10=mean(x10)
v10=variance(x10) 
m01=mean(x01)
v01=variance(x01)
m11=mean(x11)
v11=variance(x11)

for x in test :
	pr0 = probability((x[0],m00,v00),(x[1],m10,v10)) * ((len(x00)+len(x10))/1000)

	pr1 = probability((x[0],m01,v01),(x[1],m11,v11)) *((len(x01)+len(x11))/1000)
	
	print(pr0,pr1)

	if(pr0>=pr1):
		print("Class 1")
	else :
		print("Class -1")