import sys
from Tkinter import *
import tkMessageBox
import string

class Gauss:  
    def __init__(self,A,b,dim):
        self.A = A
        self.b = b
        self.n = dim

    def gaussTrivial(self):  
        n = self.n
        a = []
        for i in range(n):
	        a.append([])
	        for j in range(n):
		        a[i].append(self.A[i][j])

        for i in range(n):
	        a[i].append(self.b[i])

        maxi=0.0
        pos_maxi=-1
        cont=0
        for i in range(n-1):
	        if a[i][i] == 0:
		        for p in range(i,n):
			        if maxi< abs(a[p][i]):
				        maxi = a[p][i]
				        pos_maxi = p
		        a[i], a[p] = a[p], a[i]
	        for j in range(i+1, n):
		        h = a[j][i]/a[i][i]
		        cont+=1
		        for k in range(i, n+1):
			        a[j][k] = a[j][k] - h*a[i][k]
			        cont+=2
        x = []
        for i in range(n):
	        x.append(0.0)
	          
        ##############################
        #Imprime la matriz aumentada
        MatrizAumentada = 'Gauss Trivial:\n'

        RES = 1
        for i in range(n):
	        if a[i][i]==0:
		        RES =  0

        if RES == 1: 
	        j = n-1
	        while j>=0:
		        res = a[j][n]
		        for k in range (j+1, n):
			        res -= a[j][k] *x[k]
			        cont+=2
                        res /= float(a[j][j])
		        cont+=1
		        x[j] = res
		        j-=1
	        MatrizAumentada += '\n' + str(x) + '\n\n'
        else:
	        MatrizAumentada += '\nNO TIENE SOLUCION\n\n'        
       
        #print MatrizAumentada
        return MatrizAumentada
        
    def gaussParcial(self):
        n = self.n
        a = []
        for i in range(n):
	        a.append([])
	        for j in range(n):
		        a[i].append(self.A[i][j])

        for i in range(n):
	        a[i].append(self.b[i])

        cont_op=0
        maxi = 0
        pos_maxi=-1
        P = []
        for i in range(n):
            P.append(i)
        for i in range(n-1):
	        maxi = 0
	        pos_maxi=-1
	        for p in range(i,n):
                    if maxi< abs(a[p][i]):
                            maxi = abs(a[p][i])
                            pos_maxi = p
	        a[i], a[pos_maxi] = a[pos_maxi], a[i]
	        P[i], P[pos_maxi] = P[pos_maxi], P[i]
	        for j in range(i+1, n):
	            h = a[j][i]/a[i][i]
	            cont_op+=1
	            for k in range(i, n+1):
	                a[j][k] = a[j][k] - h*a[i][k]
	                cont_op+=2
        x = []
        for i in range(n):
	        x.append(0.0)
	          
        ##############################
        #Imprime la matriz aumentada
        MatrizAumentada = 'Gauss con Pivoteo Parcial:\n'

        RES = 1
        for i in range(n):
	    if a[i][i]==0:
		RES =  0
        
        if RES == 1: 
            j = n-1
            while j>=0:
	        res = a[j][n]
	        for k in range (j+1, n):
		        res -= a[j][k] *x[k]
		        cont_op+=2
                res /= float(a[j][j])
	        cont_op+=1
	        x[j] = res
	        j-=1
            MatrizAumentada += '\n' + str(x) + '\n\n'
        else:
            MatrizAumentada += '\nNO TIENE SOLUCION\n\n'        
        
        #print MatrizAumentada
        return MatrizAumentada

    def all(self):
        ret = ''
        ret += self.gaussTrivial()
        ret += self.gaussParcial()
        return ret
