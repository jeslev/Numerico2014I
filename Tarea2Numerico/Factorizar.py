import sys
from Tkinter import *
import tkMessageBox
import string
import math

class Factorizar:
    def __init__(self,A,dim,sym,show = True):
        self.A = A
        self.n = dim
        self.can = sym
        self.show = show
        self.graphics()
        
    def graphics(self):
        global mGui
        if(self.show):
            mGui = Toplevel()
            mGui.geometry('700x300+450+300')
            mGui.title('Factorizacion de Matrices')
            
            mbotonLU1Crout = Button(mGui, text = 'LU1 Crout ', command = self.croutUTrivial).place(x=20, y = 20)
            mbotonLU1CroutParcial = Button(mGui, text = 'LU1 Crout\nPiv. Parcial', command = self.croutUParcial).place(x=20, y = 60)
            mbotonL1UCrout = Button(mGui, text = 'L1U Crout ', command = self.croutLTrivial).place(x=20, y = 110)
            mbotonL1UCroutParcial = Button(mGui, text = 'L1U Crout\nPiv. Parcial', command = self.croutLParcial).place(x=20, y = 140)
            mbotonLDLT = Button(mGui, text = 'Metodo LDL^T ', command = self.LDLT).place(x=20, y = 190)
            mcholF = Button(mGui, text = 'Cholesky x Filas ', command = self.choleskyFilas).place(x=20, y = 220)
            mcholF = Button(mGui, text = 'Cholesky x Columnas ', command = self.choleskyColumnas).place(x=20, y = 260)
        
    def croutUTrivial(self):
        n = self.n
        a = []
        L = []
        U = []
        for i in range(n):
                a.append([])
                for j in range(n):
                        a[i].append(self.A[i][j])
        for i in range(n):
                L.append([])
                U.append([])
                for j in range(n):
                        L[i].append(0.0)
                        U[i].append(0.0)
        
        mensaje = 'Matriz A:\n'
        for i in range(n):
                mensaje += str(a[i])+'\n'
        cont = 0
 
        for k in range (n):
                for i in range(k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[i][p]*U[p][k]
                                cont+=2
                        L[i][k] = a[i][k]-res
                        cont+=1
                for i in range (k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[k][p]*U[p][i]
                                cont+=2
                        U[k][i] = (a[k][i]-res)/L[k][k]
                        cont+=2
         
        mensaje+='\nMatriz L:\n'
         
        for i in range(n):
                mensaje+= str(L[i]) + '\n'
        mensaje+= '\nMatriz U:\n'
        for i in range(n):
                mensaje += str(U[i])+'\n'
        mensaje+= '\n'
         
        mensaje += 'Numero de operaciones: '+str(cont)
        text = Text(mGui)
        text.insert(INSERT, mensaje)
        text.insert(END, '...')
        text.place(x=150,y=40)
        return L,U
        
    def croutUParcial(self):
        n = self.n
        a = []
        L = []
        U = []
        for i in range(n):
                a.append([])
                for j in range(n):
                        a[i].append(self.A[i][j])
        for i in range(n):
                L.append([])
                U.append([])
                for j in range(n):
                        L[i].append(0.0)
                        U[i].append(0.0)
        
        mensaje = 'Matriz A:\n'
        for i in range(n):
                mensaje += str(a[i])+'\n'
        cont = 0
        P = []
        for i in range (n):
            P.append(i)
        for k in range (n):
                pos = -1
                maxi = 0.0
                for i in range(k,n):   
                        if maxi < abs(a[i][k]):
                                pos = i
                                maxi = abs(a[i][k])
                a[pos], a[k] = a[k], a[pos]
               
                P[k], P[pos] = P[pos], P[k]
         
                maxi = 0.0     
                for i in range(k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[i][p]*U[p][k]
                                cont+=2
                        L[i][k] = a[i][k]-res
                        cont+=1
               
                for i in range (k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[k][p]*U[p][i]
                                cont+=2
                        U[k][i] = (a[k][i]-res)/L[k][k]
                        cont+=2
         
        mensaje+='\nMatriz L:\n'
         
        for i in range(n):
                mensaje+= str(L[i]) + '\n'
        mensaje+= '\nMatriz U:\n'
        for i in range(n):
                mensaje += str(U[i])+'\n'
        mensaje+= '\nMatriz P:\n'+str(P)+'\nMatriz A Permutada:\n'
        for i in range(n):
                mensaje+= str(self.A[P[i]])
        mensaje += '\nNumero de operaciones: '+str(cont)
        text = Text(mGui)
        text.insert(INSERT, mensaje)
        text.insert(END, '...')
        text.place(x=150,y=40)
        return L,U
        
    def croutLTrivial(self):
        n = self.n
        a = []
        L = []
        U = []
        for i in range(n):
                a.append([])
                for j in range(n):
                        a[i].append(self.A[i][j])
        for i in range(n):
                L.append([])
                U.append([])
                for j in range(n):
                        L[i].append(0.0)
                        U[i].append(0.0)
        
        mensaje = 'Matriz A:\n'
        for i in range(n):
                mensaje += str(a[i])+'\n'
        cont = 0
 
        for k in range (n):
                for j in range(k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[k][p]*U[p][j]
                                cont+=2
                        U[k][j] = a[k][j]-res
                        cont+=1
                for i in range (k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[i][p]*U[p][k]
                                cont+=2
                        L[i][k] = (a[i][k]-res)/U[k][k]
                        cont+=2
         
        mensaje+='\nMatriz L:\n'
         
        for i in range(n):
                mensaje+= str(L[i]) + '\n'
        mensaje+= '\nMatriz U:\n'
        for i in range(n):
                mensaje += str(U[i])+'\n'
        mensaje+= '\n'
         
        mensaje += 'Numero de operaciones: '+str(cont)
        text = Text(mGui)
        text.insert(INSERT, mensaje)
        text.insert(END, '...')
        text.place(x=150,y=40)
        return L,U
        
    def croutLParcial(self):
        n = self.n
        a = []
        L = []
        U = []
        for i in range(n):
                a.append([])
                for j in range(n):
                        a[i].append(self.A[i][j])
        for i in range(n):
                L.append([])
                U.append([])
                for j in range(n):
                        L[i].append(0.0)
                        U[i].append(0.0)
        
        mensaje = 'Matriz A:\n'
        for i in range(n):
                mensaje += str(a[i])+'\n'
        cont = 0
        P = []
        for i in range (n):
            P.append(i)
        for k in range (n):
                pos = -1
                maxi = 0.0
                for i in range(k,n):
                        if maxi < abs(a[i][k]):
                                pos = i
                                maxi = abs(a[i][k])
                a[pos], a[k] = a[k], a[pos]
               
                P[pos], P[k] = P[k], P[pos]
               
         
                for j in range(k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[k][p]*U[p][j]
                                cont+=2
                        U[k][j] = a[k][j]-res
                        cont+=1
                for i in range (k,n):
                        res = 0.0
                        for p in range(k):
                                res += L[i][p]*U[p][k]
                                cont+=2
                        L[i][k] = (a[i][k]-res)/U[k][k]
                        cont+=2
        mensaje+='\nMatriz L:\n'
         
        for i in range(n):
                mensaje+= str(L[i]) + '\n'
        mensaje+= '\nMatriz U:\n'
        for i in range(n):
                mensaje += str(U[i])+'\n'
        mensaje+= '\nMatriz P:\n'+str(P)+'\nMatriz A Permutada:\n'
        for i in range(n):
                mensaje+= str(self.A[P[i]])
        mensaje += '\nNumero de operaciones: '+str(cont)
        text = Text(mGui)
        text.insert(INSERT, mensaje)
        text.insert(END, '...')
        text.place(x=150,y=40)
        return L,U 

    def LDLT(self):
        if not self.can:
            tkMessageBox.showinfo('AVISO!', 'La matriz no es simetrica!')
            return
        n = self.n
        a = []
        L = []
        U = []         
        for i in range(n):
                a.append([])
                for j in range(n):
                        a[i].append(self.A[i][j])
         
        for i in range(n):
                L.append([])
                U.append([])
                for j in range(n):
                        L[i].append(0.0)
                        U[i].append(0.0)
        mensaje = 'Matriz A:\n'
        for i in range(n):
                mensaje += str(a[i])+'\n'
        cont = 0         
        D = []
        for i in range(n):
                D.append([])
                for j in range(n):
                        D[i].append(0.0)
         
        for k in range (n):
                res = 0.0;
                for p in range(k):
                        res += a[k][p]*a[k][p]*D[p][p]
                        cont+=2
                       
                D[k][k] = a[k][k]-res
                cont+=1
               
                if D[k][k]==0:
                        break
               
                for i in range (k,n):
                        res = 0.0
                        for p in range(k):
                                res += a[i][p]*a[k][p]*D[p][p]
                                cont+=2
                        a[i][k] = (a[i][k]-res)/D[k][k]
                        cont+=2
        mensaje +='\nMatriz a al final de las operaciones: \n'
        for i in range(n):
                mensaje += str(a[i])+'\n'         
         
        mensaje += '\nMatriz diagonal (D):\n'
        for i in range(n):
                mensaje += str(D[i]) + '\n'
        LL,UU = self.croutLParcial()
        mensaje += '\nMatriz L:\n'
        for i in range(n):
                mensaje += str(LL[i])+'\n'   
        mensaje += '\nNumero de operaciones: '+str(cont)
        text = Text(mGui)
        text.insert(INSERT, mensaje)
        text.insert(END, '...')
        text.place(x=150,y=40)
        return LL,UU
        
    def choleskyFilas(self):
        if not self.can:
            tkMessageBox.showinfo('AVISO!', 'La matriz no es simetrica!')
            return
        n = self.n
        a = []
        GT = []
        G = []
        
        for i in range(n):
                a.append([])
                for j in range(n):
                        a[i].append(self.A[i][j])
         
        for i in range(n):
                GT.append([])
                G.append([])
                for j in range(n):
                        G[i].append(0.0)
                        GT[i].append(0.0)
        mensaje = 'Matriz A:\n'
        for i in range(n):
                mensaje += str(a[i])+'\n'
        cont = 0         
        for i in range (n):
                res = 0.0
                for k in range(i):
                        res += GT[k][i]*GT[k][i]
                        cont+=2
                GT[i][i] = math.sqrt(a[i][i]-res)
                cont+=1
                for j in range (i,n):
                        res = 0.0
                        for k in range(i):
                                res += GT[k][i]*GT[k][j]
                                cont+=2
                        GT[i][j] = (a[i][j]-res)/GT[i][i]
                        cont+=2
        for i in range(n):
                for j in range(n):
                        G[i][j] = GT[j][i]
                        
        mensaje += '\nMatriz G:\n'
        for i in range(n):
                mensaje += str(G[i]) + '\n'
        mensaje += '\nMatriz GT:\n'
        for i in range(n):
                mensaje += str(GT[i]) + '\n'
        mensaje += '\nNumero de operaciones: '+str(cont)
        text = Text(mGui)
        text.insert(INSERT, mensaje)
        text.insert(END, '...')
        text.place(x=150,y=40)
        return G,GT
        
    def choleskyColumnas(self):
        if not self.can:
            tkMessageBox.showinfo('AVISO!', 'La matriz no es simetrica!')
            return
        n = self.n
        a = []
        GT = []
        G = []
        for i in range(n):
                a.append([])
                GT.append([])
                for j in range(n):
                        if j>=i:
                                a[i].append(self.A[i][j])
                                GT[i].append(self.A[i][j])
                        else:
                                GT[i].append(0.0)
                                a[i].append(self.A[i][j])
        for i in range(n):
                G.append([])
                for j in range(n):
                        G[i].append(0.0)
        mensaje = 'Matriz A:\n'
        for i in range(n):
                mensaje += str(a[i])+'\n'
        cont = 0
        info = 1
        for j in range (n):
                for i in range(j):
                        res = 0.0
                        for k in range(i):
                                res += GT[k][i]*GT[k][j]
                                cont+=2
                        GT[i][j] = (GT[i][j]-res)/GT[i][i]
                        cont+=2
                        #print i, j, a[i][j]
                       
                res = 0.0
                for k in range (j):
                        res += GT[k][j]*GT[k][j]
                        cont+=2
                print j               
                temp = GT[j][j]-res
                if temp<=0:
                        info = 0
                        break
                GT[j][j] = math.sqrt(temp)
                #GT[j][j] = math.sqrt(a[j][j]-res)
                cont+=2
                #print j, a[j][j]
        info = 1
        for i in range(n):
                for j in range(n):
                        G[i][j] = GT[j][i]
        mensaje += '\nMatriz G:\n'
        for i in range(n):
                mensaje += str(G[i]) + '\n'
        mensaje += '\nMatriz GT:\n'
        for i in range(n):
                mensaje += str(GT[i]) + '\n'
        mensaje += '\nNumero de operaciones: '+str(cont)
        text = Text(mGui)
        text.insert(INSERT, mensaje)
        text.insert(END, '...')
        text.place(x=150,y=40)
        return G,GT
