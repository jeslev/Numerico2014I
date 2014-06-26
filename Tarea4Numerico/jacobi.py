import string
from  math import *
from copy import *
import numpy

class Jacobi():

    def __init__(self,A,B,m,n):
        X_0 = [ 0 for i in range(n)]
        ep = 0.00001
        self.J = []
        self.txt = self.jacobi(A,B,X_0,ep,min(m,n),n)
            
        
    def getTxt(self):
        return self.txt
    
    def getJ(self):
        return self.J
        
    def jacobi(self,matrixA, matrixB, matrixX_0, precision,n,nn):
        x =matrixX_0
        D = deepcopy(matrixA)
        a = deepcopy(matrixA)
        y =[]
        b = deepcopy(matrixB)
        prec = deepcopy(precision)
        s1= su= x1=0.0
        J = []
        if len(a)==len(a[0]):
            for i in range(n):
                for j in range(n):
                    if i!=j:
                        D[i][j]=0.0
            D = numpy.linalg.inv(D)
            d=[[0 for i in range(n)] for j in range(n)]            
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        d[i][j] += (D[i][k]*a[k][j])                 
            
            J = numpy.identity(n)
            J = J-d
            
        for i in range (nn):
            y.append(0.0)
        
        it = 0
        resu='\n\n\t\t\t\t\tMETODO JACOBI\nVALORES DE X^(i):\n' +"0 -- " + str(x) + "\n"
        for i in range(n):
		    if a[i][i] == 0:
			    return 'Los elementos A[i][i] deben ser diferentes de 0'
         
        for j in range(n):
            dominancia = 0.0
            for i in range(n):
                if j != i:
				    dominancia += fabs(a[i][j])
            if a[j][j] < dominancia:
			    return 'La matriz no converge'
        while True:
            s1=0.0
            it+=1
            for i in range (n):
                su=b[i] ## el b inicia desde posicion 0
                
                for j in range (i):
                    su -= a[i][j]*x[j]

                for j in range (i+1,n):            
                    su -= a[i][j]*x[j]

                y[i]=su/a[i][i]
                s1 = max(s1, abs(y[i]) )
            sm=0.0
            
            for i in range (n):
                sm= max( abs(x[i]-y[i])/s1 , sm)
                x[i] = y[i]  

            resu += (str(it) + " -- "+ str(x) + "\n")

            if sm<=prec:
                resu += "\nLA SOLUCION FINAL ES:\n" + str(x) + "\n\nY LA CONVERGENCIA ES:  " + str(sm) + "\n\n"
                self.J = J
                return resu

