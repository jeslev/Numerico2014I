from random import *

class Sor():

    def __init__(self,A,B,W):
        x_0 = [ 0 for i in range(len(A))]
        ep = 0.000001
        self.txt =self.SOR(A, B, x_0, W,ep)
        self.txt += "\nPESO ALEAOTORIO" + str(W)
        
    def getTxt(self):
        return self.txt        
    
    def SOR(self,matrixA, matrixB, matrixX_0,weight,precision):
        a = matrixA
        b = matrixB
        w = weight
        n = len(a)
        x = matrixX_0
        prec = precision
        s1 = su = sm = xi = float(0)
        sm = 1.0
        it = 0
        for i in range(n):
            if a[i][i]==0.0:
                return "ERROR: Todos los elementos de la diagonal deben ser distintos de CERO"
        ret = "\n\t\t\t\tMETODO SOR\n\nVALORES DE Xi: \n"    #retorna todos los valores en x;
        ret = ret + "0 -- " + str(x) + "\n"
        while sm >= prec:
            it += 1 
            s1 = 0.0
            sm = 0.0
            for i in range(n):
                su = b[i]
                for j in range (i):
                    su = su - a[i][j]*x[j]
                
                for j in range (i+1, n):
                    su = su - a[i][j]*x[j]
                xi = (1-w)*x[i]+w*su/a[i][i]
                sm = max(abs(x[i]-xi), sm)
                x[i] = xi
                s1 = max(s1, abs(x[i]))
            sm = sm/s1
            ret += (str(it) + " -- "+ str(x) + "\n")
            
        ret += "\nLA SOLUCION FINAL ES:\n" + str(x) + "\n\nY LA CONVERGENCIA ES:  " + str(sm)+"\n\n"
        return ret   #retorna el string paso a paso para cada x, y la respuesta al problema

