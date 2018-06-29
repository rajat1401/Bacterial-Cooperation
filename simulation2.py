#k centred focused movement of bacterial cells under antibiotic stress!

import numpy as np
import random as rand
import math

def getNeighbour(a, b):#perfecto
	list= []
	if(a>0 and a<matrixSize - 1):
		list.append(a+1)
		list.append(b)
		list.append(a-1)
		list.append(b)
		if(b< matrixSize - 1):
			list.append(a)
			list.append(b+1)
		if(b> 0):
			list.append(a)
			list.append(b-1)
	elif(a== 0):
		if(b>0 and b<matrixSize - 1):
			list.append(a)
			list.append(b-1)
			list.append(a)
			list.append(b+1)
			list.append(a+1)
			list.append(b)
		elif(b== 0):
			list.append(a+1)
			list.append(b)
			list.append(a)
			list.append(b+1)
		else:
			list.append(a+1)
			list.append(b)
			list.append(a)
			list.append(b-1)
	else:#a is 49
		if(b> 0 and b< matrixSize - 1):
			list.append(a)
			list.append(b-1)
			list.append(a)
			list.append(b+1)
			list.append(a-1)
			list.append(b)
		elif(b== matrixSize - 1):
			list.append(a)
			list.append(b-1)
			list.append(a-1)
			list.append(b)
		else:
			list.append(a-1)
			list.append(b)
			list.append(a)
			list.append(b+1)

	return list


def dist(a, b):
	return math.sqrt((bactx[a] - bactx[b])**2 + (bacty[a] - bacty[b])**2)


def findkcentres():
	list1= []
	list2= []
	list3= []
	for i in range(100):
		d1= dist(i, anti[0])
		d2= dist(i, anti[1])
		d3= dist(i, anti[2])
		a= min(d1, d2, d3)
		if(a== d1):
			list1.append(i)
		elif(a== d2):
			list2.append(i)
		else:
			list3.append(i)

	#make this modular!
	list= []
	sum1= 0
	sum2= 0
	for i in range(len(list1)):
		sum1+= bactx[list1[i]]
		sum2+= bacty[list1[i]]
	list.append(sum1/len(list1))
	list.append(sum2/len(list1))

	for i in range(len(list2)):
		sum1+= bactx[list2[i]]
		sum2+= bacty[list2[i]]
	list.append(sum1/len(list2))
	list.append(sum2/len(list2))

	for i in range(len(list3)):
		sum1+= bactx[list3[i]]
		sum2+= bacty[list3[i]]
	list.append(sum1/len(list3))
	list.append(sum2/len(list3))

	return list


def movespecial(k):#move towards the k centres of the populations



def inviscinity(k):#check if itself antibiotic resistant, then meaningless
	if(matrix[bactx[k]][bacty[k]]!= -1):
		list= getNeighbour(bactx[k], bacty[k])
		for i in range(len(list)/2):
			if(matrix[list[2*i]][list[2*i + 1]]== -1):
				return True

	return False



global matrixSize
matrixSize= 25
numsims= 100
global matrix
matrix = np.zeros((matrixSize, matrixSize), dtype= 'int32')
global bactx
bactx = [0]*100
global bacty
bacty = [0]*100
psafe= [0]*100
aplha= 0.5
beta= 0.20
anti= []

for i in range(100):
	a= rand.randint(0, matrixSize - 1)
	b= rand.randint(0, matrixSize - 1)
	matrix[a][b]= 1
	bactx[i]= a
	bacty[i]= b


for i in range(3):
	a= rand.randint(1, 100)
	matrix[bactx[a-1]][bacty[a-1]]= -1#antibiotic resistant bacteria!
	anti.append(a)


for i in range(numsims):
	for j in range(100):
		for k in range(100):
			if(inviscinity(k)):
				psafe[k]+= 0.02

		for k in range(len(anti)):
			movespecial(anti[k])

		if(j%3== 0):
			for k in range(len(anti)):
				a= rand.uniform(0, 1)
				if(a<= beta):
					matrix[bactx[anti[k] - 1][bacty[anti[k] - 1]]= 1#makes it normal
					anti[k]= rand.randint(1, 100)
					matrix[bactx[anti[k] - 1]][bacty[anti[k]-1]]= -1#makes the new one antibiotic resistant


for i in range(len(anti)):
	psafe[anti[i]-1]= 1

for i in range(100):
	if(invinscinity(i)):
		psafe[i]= min(psafe[i], aplha)
