import sys
from Tkinter import *
from Factorizar import *
import tkMessageBox
import string

class Solver:
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
        mGui.title('Solucion de Ecuaciones lineales')
        mlabel1 = Label(mGui, text= 'Ingrese columna B \n(dejando espacios)').place(x=20,y=20)  
        mbetha = Entry(mGui, textvariable = colB).place(x=200,y=20)
            
        mbotonLU1Crout = Button(mGui, text = 'L1U Crout ', command = self.croutLTrivialsolve).place(x=20, y = 60)
        mbotonLU1CroutP = Button(mGui, text = 'L1U Crout\nParcial ', command = self.croutLTrivialsolve).place(x=20, y = 110)
        mbotonL1UCrout = Button(mGui, text = 'LU1 Crout ', command = self.croutLTrivialsolve).place(x=20, y = 150)
        mbotonL1UCroutParcial = Button(mGui, text = 'L1U Crout\nPiv. Parcial', command = self.croutLTrivialsolve).place(x=20, y = 190)
        mbotonLDLT = Button(mGui, text = 'Metodo LDL^T ', command = self.croutLTrivialsolve).place(x=20, y = 230)
        mcholF = Button(mGui, text = 'Cholesky x Filas ', command = self.croutLTrivialsolve).place(x=20, y = 270)
        mcholF = Button(mGui, text = 'Cholesky x Columnas ', command = self.croutLTrivialsolve).place(x=20, y = 300)
        
    def getBMatrix(self):
        global colB,b
        B = colB.get()
        numsB = B.split()
        for i in numsB:
            b.append(float(i))
        
    def croutLTrivialsolve(self):
        self.getBMatrix()
        S = Factorizar(self.A,self.n, True,True)
        L, U = S.croutLTrivial()
        j = 0
        y = []
        a=self.A
        n = self.n
        for i in range(n):
            y.append(0.0)
        while j < n:
	        res = b[j]
	        for k in range (j):
		        res -= L[j][k] *y[k]
		        #cont_op+=2
	        res /= float(L[j][j])
	        #cont_op+=1
	        y[j]=res
	        j+=1
        j = n-1
        x=[]
        for i in range(n):
            x.append(0.0)
        while j>=0:
	        res = y[j]
	        for k in range (j+1, n):
		        res -= U[j][k] *x[k]
		        #cont_op+=2
	        res /= float(U[j][j])
	        #cont_op+=1
	        x[j] = res
	        j-=1
        tkMessageBox.showinfo('AVISO!', str(x))
