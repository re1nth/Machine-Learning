# python3 programming_2.py
import csv

finput = "X.csv"
foutput = "Y.csv"

Data = []
x1 = []
x2 = []
y = []
K = [4,10,50,300,500,1000]
test=[[1,1],[1,-1],[-1,1],[-1,-1]]

# calculation of euclidean distance between the points
def dist(inp1, inp2) :
	px1 = float(inp1[0])
	py1 = float(inp1[1])
	px2 = float(inp2[0])
	py2 = float(inp2[1])
	ans  = (px1-px2)*(px1-px2)
	ans = ans + (py1-py2)*(py1-py2)
	return ans

# sort the points according to the distance and calculate the average of first k points
def sort(inp,k):
	# used selection sort for fewer number of swaps
	for i in range(0,1000):
		dis = float(inp[i][0])
		f = i 
		s = -1
		for j in range(i+1,1000):
			cur = float(inp[j][0])	
			if(cur<dis) :
				s = j
				dis = cur	
		if(s!=-1):
			p = float(inp[f][0])
			q = float(inp[f][1])
			inp[f]=(float(inp[s][0]),float(inp[s][1]))
			inp[s]= (p,q) 
	avg = 0.0		
	for i in range(0,k) :
		avg = avg + float(inp[i][1])
	return avg 			

with open(finput,'r') as csvfile :

	csvreader = csv.reader(csvfile)

	i = 0 
	for row in csvreader : 
		j = 1
		for elements in row :
			if(i==0) :  
				x1.append(elements)
			else :
				x2.append(elements)		
		i = i + 1		

with open(foutput,'r') as csvfile :

	csvreader = csv.reader(csvfile)

	for row in csvreader :
		for elements in row : 
	 		y.append(elements)	 	
	 			
for k in range(0,1000):	
	Data.append((float(x1[k]),float(x2[k]),float(y[k])))

# calc(Data)

for k in K:
	for i in range(0,4):
		klist = [1000*[0]]
		finp = test[i]
		for j in range(0,1000) : 	
			klist .append((dist(finp,Data[j]),y[j]))
		avg = sort(klist,int(k))
		if(avg>=0) :
			print("K =",k,"Class 1")
		else :
			print("K =",k,"Class -1")		