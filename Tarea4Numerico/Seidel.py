from math import *
from copy import *
import numpy
class GaussSeidel():

    def __init__(self,A,b,m,n):
        self.G = []
        self.txt = self.gaussSeidel(A,b,min(m,n),n)
    
    
    def getTxt(self):
        return self.txt

    def getG(self):
        return self.G
        
    def normaInfVector(self,L):
	    """ Calcula la norma infinita de un vector:
		    ||x|| = max {|xi|}, i = 0, 1, ... n.
	    """

	    maximum = fabs(L[0])
	    for i in range(1, len(L)):
		    maximum = max(maximum, fabs(L[i]))
	    return maximum	

    def gaussSeidel(self,A, b, n,nn,prec=1e-7):
        print nn
        Xk = [0.0 for i in range(nn)]
        D = deepcopy(A)
        F = deepcopy(A)
        if (len(A)==len(A[0])):
            for i in range(n):
                for j in range(n):
                    if i<j:
                        D[i][j] = 0.0
                    elif i > j:
                        D[i][j]*= -1.0
                        F[i][j] = 0.0
                    else: 
                        F[i][j] = 0.0 
            D = numpy.linalg.inv(D)
            G=[[0 for i in range(n)] for j in range(n)]            
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        G[i][j] += (D[i][k]*F[k][j])
            self.G = G
        
        	    
        sumation = 0.0
        it = 0
        resu='\n\n\t\t\t\t\tMETODO GAUSS-SEIDEL\nVALORES DE X^(i):\n' +"0 -- " + str(Xk) + "\n"
        for i in range(n):
            if A[i][i] == 0:
	            return 'ERROR\nLos elementos A[i][i] deben ser diferentes de 0'
        Xk1 = [b[i]/float(A[i][i]) for i in range(n)]
        minus = lambda x, y: [x[i]-y[i] for i in range(n)]

        for j in range(n):
            dominancia = 0.0
            for i in range(n):
	            if j != i:
		            dominancia += fabs(A[i][j])
            if A[j][j] < dominancia:
	            return 'ERROR\nLa matriz no converge'

        while (self.normaInfVector(minus(Xk1,Xk)) / float(self.normaInfVector(Xk1))) > prec:
            Xk[:] = Xk1[:]
            for i in range(n):
	            sumation1 = sum(A[i][j]*Xk1[j] for j in range(i))
	            sumation2 = sum(A[i][j]*Xk1[j] for j in range(i+1, n))

	            Xk1[i] = (1.0/A[i][i])*(b[i] - sumation1 - sumation2)

            resu += (str(it) + " -- "+ str(Xk) + "\n")
            it+=1
            print self.normaInfVector(minus(Xk1, Xk)), self.normaInfVector(Xk1)
        for i in range(nn-n):
            Xk.append(0.0)
        resu += "\nLA SOLUCION FINAL ES:\n" + str(Xk) + '\n'	
        return resu

