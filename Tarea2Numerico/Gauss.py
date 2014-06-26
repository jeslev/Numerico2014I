import sys
from Tkinter import *
from Factorizar import *
import tkMessageBox
import string

class Gauss:  
    def __init__(self,A,dim):
        self.A = A
        self.n = dim
        self.graphics()
        
    def graphics(self):
        global colB,b,mGui
        b = []
        colB = StringVar()
        mGui = Toplevel()
        mGui.geometry('700x300+450+300')
        mGui.title('Solucion de Ecuaciones lineales por Gauss')
        mlabel1 = Label(mGui, text= 'Ingrese columna B \n(dejando espacios)').place(x=20,y=20)  
        mbetha = Entry(mGui, textvariable = colB).place(x=200,y=20)
            
        mbotonTrivial = Button(mGui, text = 'Pivotacion trivial', command = self.gaussTrivial).place(x=20, y = 100)
        mbotonParcial = Button(mGui, text = 'Pivotacion parcial', command = self.gaussParcial).place(x=20, y = 140)
        
    def getBMatrix(self):
        global colB,b
        B = colB.get()
        numsB = B.split()
        for i in numsB:
            b.append(float(i))
        
    def gaussTrivial(self):  
        n = self.n
        #Los dos for siguientes me crean la matriz aumentada a = [A|b]        
        self.getBMatrix()
        a = []
        for i in range(n):
	        a.append([])
	        for j in range(n):
		        a[i].append(self.A[i][j])

        for i in range(n):
	        a[i].append(b[i])

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
        MatrizAumentada = 'Matriz aumentada final:\n\n'

        for i in range(n):
	        for j in range(n+1):
		        MatrizAumentada += str(a[i][j])+ ' '
	        MatrizAumentada+='\n' 

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
	        MatrizAumentada += '\nValores de xi (i=1 ...n ) =' 
	        MatrizAumentada += str(x)
	        MatrizAumentada += '\ncontador de operaciones: ' + str(cont)
        else:
	        MatrizAumentada += '\nNO TIENE SOLUCION'        
        text = Text(mGui)
        text.insert(INSERT, MatrizAumentada)
        text.insert(END, '...')
        text.place(x=150,y=40)
        #print MatrizAumentada
        return
        
    def gaussParcial(self):
        n = self.n
        #Los dos for siguientes me crean la matriz aumentada a = [A|b]        
        self.getBMatrix()
        a = []
        for i in range(n):
	        a.append([])
	        for j in range(n):
		        a[i].append(self.A[i][j])

        for i in range(n):
	        a[i].append(b[i])

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
        MatrizAumentada = 'Matriz aumentada final:\n\n'

        for i in range(n):
	        for j in range(n+1):
		        MatrizAumentada += str(a[i][j])+ ' '
	        MatrizAumentada+='\n' 
 
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
        MatrizAumentada += '\nValores de xi (i=1 ...n ) =' 
        MatrizAumentada += str(x)
        MatrizAumentada += '\ncontador de operaciones: ' + str(cont_op)
        MatrizAumentada += '\nMatriz P de permutacion\n' + str(P)
        text = Text(mGui)
        text.insert(INSERT, MatrizAumentada)
        text.insert(END, '...')
        text.place(x=150,y=40)
        #print MatrizAumentada
        #self.croutLParcialsolve()
        return
