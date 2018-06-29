#Random simulation of the bacterial movement under antibiotic attack.

import numpy as np
import random as rand

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


def move(a, b, k):#returns nothing since now all things are global 
	list= getNeighbour(a, b)
	c= rand.randint(0, len(list)/2 - 1)#inclusive of both
	if(matrix[list[2*c]][list[2*c + 1]]== 0):#move there
		matrix[list[2*c]][list[2*c + 1]]= matrix[a][b]
		matrix[a][b]= 0
		bactx[k]= list[2*c]
		bacty[k]= list[2*c + 1]


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
	matrix[a][b]= 1#for normal bacteria!
	bactx[i]= a
	bacty[i]= b

for i in range(3):
	a= rand.randint(1, 100)
	matrix[bactx[a-1]][bacty[a-1]]= -1#antibiotic resistant bacteria!
	anti.append(a)


#simulation of the random movement!
for i in range(numsims):
	for j in range(100):#100 bacteria each is moving 100 times!
		for k in range(100):
			if(inviscinity(k)):
				psafe[k]+= 0.02

		for k in range(100):
			move(bactx[k], bacty[k], k)

		#now someone else takes up the antibiotic properties(maybe)!
		if(j%3== 0):
			for m in range(3):
				a= rand.uniform(0, 1)
				if(a<= beta):
					matrix[bactx[anti[m]-1]][bacty[anti[m]-1]]= 1
					anti[m]= rand.randint(1, 100)
					matrix[bactx[anti[m]-1]][bacty[anti[m]-1]]= -1

		


psafe[anti[0]-1]= 1
psafe[anti[1]-1]= 1
psafe[anti[2]-1]= 1
for i in range(100):
	if(invinscinity(i)):
		psafe[i]= min(psafe[i], aplha)







