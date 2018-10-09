from math import exp
from random import *
import numpy as np

seed(0)

# Given input
inps= [[1, 1], [1, 0], [0, 1], [0, 0]]

# hiden nodes
Hn = 2

# T output
T = {}
T= [1, 1, 1, 0]

# number of training inpsuts
N=100000

# Generate random hidden weights 
HW = {}
HW= [[random(), random()] for i in range(Hn)]
# Generate random output weights
OW = {}
OW= [random() for i in range(Hn)]

# Bias1 and Bias2 
B1 = random()
B2 = random()

# learning rate
LR = 0.2

def sigmoid(val): # activation function 
    return 1/(1+np.exp(-val))

def orop(val1, val2):
    neth = [B1] * Hn
    outh = [0] * Hn
    neto = B2

    for i in range(Hn):
        neth[i] = neth[i] + val1 * HW[i][0] + val2 * HW[i][1]
        outh[i] = sigmoid(neth[i])
        neto = neto+ outh[i] * OW[i]
    outo = sigmoid(neto)    
    return (outh, outo)

for i in range(N):
    for j in range(4) :
        outh, outo = orop(inps[j][0], inps[j][1])

        delo = (outo - T[j]) * outo * (1 - outo)
        
        for k in range(Hn):
            delh = OW[k] * delo * outh[k] * (1 - outh[k]) 
            OW[k] -= LR * delo * outh[k]
            HW[k][0] -= LR * delh * inps[j][0]
            HW[k][1] -= LR * delh * inps[j][1]

for i in inps:
    inps1 = i[0]
    inps2 = i[1]
    print(f"{inps1} or {inps2} =", orop( inps1, inps2))