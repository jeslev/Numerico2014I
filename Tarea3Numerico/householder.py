from  math import *
m=3
n=2
A= [[3,-6], [4,-8], [0,1]]
b = [-1,7,2]
X = [0]*m
#Transformacion de Matriz A, columnas 1 a n
def houseHolder():
	w = [0]*m
	for j in range (n):
		#sacamos maximo de columnas
		MaxCol = A[j][j]
		for k in range(j+1,m):
			MaxCol = max(MaxCol, A[k][j])
		if MaxCol==0:
			return -1
		psum = 0
		for k in range (j,m):
			psum = psum + A[k][j]*A[k][j]
		ssign = copysign(1,A[j][j])
		sigma = sqrt(psum)*ssign
		for k in range (j,m):
			w[k] = A[k][j]
		w[j] = w[j]+sigma
		betha = 0
		psum = 0
		for k in range(j,m):
			psum = psum+ w[k]*w[k]
		betha = float(2/psum)
		A[j][j] = -sigma
		for l in range(j+1,n):
			s = 0
			for k in range(j,m):
				s = s+w[k]*A[k][l]
			for k in range(j,m):
				A[k][l] = A[k][l]-w[k]*s*betha
		#Transformar vector B
		s = 0
		for k in range(j,m):
			s = s+w[k]*b[k]
		for k in range(j,m):
			b[k] = b[k] - w[k]*s*betha

	#limpiar Matriz A
	for x in range(n):
		for y in range(n):
			if x>y:
				A[x][y]=0
	for x in range(n,m):
		b[x]=0
		for y in range(n):
			A[x][y]=0


def solHouseHolder():
	j = n-1
	while j>=0:
		psum = 0
		for k in range(j+1,n):
			psum = psum + A[j][k]*X[k]
		X[j] = float((b[j]-psum)/A[j][j])
		j=j-1

def residuosCuadrado():
	res = 0
	for k in range(n,m):
		res = res + b[k]*b[k]
	print res

if __name__ == "__main__":
	houseHolder()
	print A
	print b
	solHouseHolder()
	print X
	residuosCuadrado()
