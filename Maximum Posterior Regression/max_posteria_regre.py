# $python3 max_post_regre.py
import numpy as np		
import matplotlib.pyplot as plt

# Number of training samples
N = [5,45]
cnt = 0
for a in N :
	# Generate N equispaced floats in the interval [0, 2π]
	x = np.linspace(0, 2*np.pi, a)
	# Generate noise
	mean = 0
	std = 0.05
	# Generate some numbers from the sine function
	y = np.matrix(np.sin(x))
	# Add noise
	y += np.random.normal(mean, std, a)
	# create a matrix Y of space n*1
	Y = np.matrix(np.transpose(y))
	# dimension of the polynomial
	D = 10
	# create an array of ones
	o1=np.ones(a) 
	# create transpose of input matrix X i.e XT
	XT=np.matrix(np.vstack((o1,x)))
	for i in range(2,D+1) :
		nx=np.power(x,i)
		XT=np.matrix(np.vstack((XT,nx)))
	# create input matrix X
	X=np.matrix(np.transpose(XT))
	# number of test data points to plot
	M= 50
	# Generate M equispaced test data floats in the interval [0, 2π]
	t =np.linspace(0,2*np.pi,M)
	# calculate XT*X 
	R = np.matrix(np.dot(XT,X))
	# Set L as lambda parameter
	alpha = int(input("Enter alpha :"))
	beta = int(input("Enter beta : "))
	# Create an identity matrix of space D+1 * D+1
	V = np.identity(D+1,dtype=float)
	# mutliply by lambda for identity
	L = alpha /beta
	V = L*V
	# add L*I to XT*X
	R = R + V
	# calculate inverse of R
	XI=np.matrix(np.linalg.inv(R))
	# calculate XT*Y
	S= np.matrix(np.dot(XT,Y))
	# calculate final parameter matrix of space n*1
	W = np.matrix(np.dot(XI,S))
	# create a vector of ones
	o2=np.ones(M)
	# create a test matrix with polynomial elements
	T=np.matrix(np.vstack((o2,t)))
	for i in range(2,D+1) :
		nx=np.power(t,i)
		T=np.matrix(np.vstack((T,nx)))
	T=np.matrix(np.transpose(T))
	# final predicted labels
	A=np.matrix(np.dot(T,W))
	# final plot of the labels for the test data
	if(cnt<=2):
		plt.text(3,200, 'train_data ='+str(a)+'\n'+'test_data= '+str(M))
	else :
		plt.text(4,0.75, 'train_data ='+str(a)+'\n'+'test_data= '+str(M))
	plt.plot(np.matrix(x),y,'ro')
	plt.plot(np.matrix(t),np.transpose(A),'go')
	plt.xlabel('x - axis')
	plt.ylabel('y - axis')
	plt.show()