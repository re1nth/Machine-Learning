# $python3 linear_reg.py
import numpy as np		
import matplotlib.pyplot as plt

# Number of training samples
N = [5,30,45,70]
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
	# create Y matrix of space n*1
	Y=np.matrix(np.transpose(y))
	# create an array of ones
	o1=np.ones(a)
	# create transpose of input matrix X as XT
	XT=np.matrix(np.vstack((o1,x)))
	# create input matrix X
	X=np.matrix(np.transpose(XT))
	# number of test data points to plot
	M= 50
	# Generate M equispaced test data floats in the interval [0, 2π]
	t =np.linspace(0,2*np.pi,M)
	# calculate XT*X 
	R = np.matrix(np.dot(XT,X))
	# calculate inverse of R
	XI=np.matrix(np.linalg.inv(R))
	# calculate XT*Y
	S= np.matrix(np.dot(XT,Y))
	# calculate final parameter matrix of n*1
	W = np.matrix(np.dot(XI,S))
	# create a vector of ones
	o2=np.ones(M)
	# create a test matrix
	T=np.matrix(np.transpose(np.matrix(np.vstack((o2,t)))))
	# final predicted labels
	A=np.matrix(np.dot(T,W))
	# final plot of the labels for the test data
	# plt.text(5,1.0,'a= 'a 'b= 'b)
	plt.text(4,0.75, 'train_data ='+str(a)+'\n'+'test_data= '+str(M))
	plt.plot(np.matrix(x),y,'ro')
	plt.plot(np.matrix(t),np.transpose(A),'go')
	plt.xlabel('x - axis')
	plt.ylabel('y - axis')
	plt.show()