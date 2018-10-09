# $python3 max_likelihood.py
import numpy as np		
import matplotlib.pyplot as plt

# Number of training samples
N = [30,45]
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
	# create Y matrix of space n*1
	Y=np.matrix(np.transpose(y))
	# dimension of the polynomial
	D = [10,30]
	# trying different dimensions for polynomial
	for b in D :
		# create an array of ones
		o1=np.ones(a) 
		# create transpose of input matrix X i.e XT
		XT=np.matrix(np.vstack((o1,x)))
		for i in range(2,b+1) :
			nx=np.power(x,i)
			XT=np.matrix(np.vstack((XT,nx)))
		# create input matrix X
		X=np.matrix(np.transpose(XT))
		# number of test data points to plot
		M= 50
		# Generate M equispaced test data floats in the interval [0, 2π]
		cnt = cnt + 1
		t =np.linspace(0,2*np.pi,M)
		# calculate XT*X 
		R = np.matrix(np.dot(XT,X))
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
		for i in range(2,b+1) :
			nx=np.power(t,i)
			T=np.matrix(np.vstack((T,nx)))
		T=np.matrix(np.transpose(T))
		# final predicted labels
		A=np.matrix(np.dot(T,W))
		# calculate ( Y - XW )
		F = np.matrix(Y-np.dot(X,W))
		# calculate variance = (Y-XW)^T * (Y-XW)
		F = np.matrix(np.dot( np.transpose(F),F))
		# variance is 0x0 element of F
		var = (F.item(0,0)/a)
		# final plot of the labels for the test data
		if(cnt<=2):
			plt.text(2,8,'train_data ='+str(a)+'\n'+'test_data= '+str(M)+'\n'+'variance= '+str(var))
		else :
			plt.text(4,0.75, 'train_data ='+str(a)+'\n'+'test_data= '+str(M)+'\n'+'variance= '+str(var))
		plt.plot(np.matrix(x),y,'ro')
		plt.plot(np.matrix(t),np.transpose(A),'go')
		plt.xlabel('x - axis')
		plt.ylabel('y - axis')
		plt.show()