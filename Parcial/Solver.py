import sys
from Factorizar import *
import string

class Solver:
    def __init__(self,A,b,dim):
        self.A = A[:]
        self.b = b[:]
        self.n = dim
        self.S = Factorizar(self.A, self.n, True, self.b)
        self.all()

    def croutTrivialL1U(self):
        L, U, correct = self.S.croutUTrivial()
        ret = str(self.solveLU(L,U, self.b))
        return ret
    
    def croutParcialL1U(self):
        L, U, correct, bb = self.S.croutUParcial()
        ret = str(self.solveLU(L,U, bb))
        return ret
    
    def croutTrivialLU1(self):
        L, U, correct = self.S.croutLTrivial()
        ret = str(self.solveLU(L,U, self.b))
        return ret
    
    def croutParcialLU1(self):
        L, U, correct, bb = self.S.croutLParcial()
        ret = str(self.solveLU(L,U, bb))
        return ret
    
    def choleskyPorFilas(self):
        L, U, correct = self.S.choleskyFilas()
        ret = str(self.solveLU(L,U, self.b))
        return ret
    
    def choleskyPorColumnas(self):
        L, U, correct = self.S.choleskyColumnas()
        ret = str(self.solveLU(L,U, self.b))
        return ret

    def solveLU(self, L, U, bb):
        error = 'NO TIENE SOLUCION'
        b = bb[:]
        j = 0
        y = []
        a=self.A[:]
        n = self.n
        for i in range(n):
            y.append(0.0)
        RES = 1
        for i in range(n):
            if L[i][i] == 0:
                RES = 0
        
        if RES == 1:
            while j < n:
                res = b[j]
                for k in range (j):
                    res -= L[j][k] *y[k]
                res /= float(L[j][j])
                y[j]=res
                j+=1
            j = n-1
        else:
            return error

        x=[]
        for i in range(n):
            x.append(0.0)
        RES = 1
        for i in range(n):
            if U[i][i] == 0:
                RES = 0
        
        if RES == 1:
            while j>=0:
                res = y[j]
                for k in range (j+1, n):
                    res -= U[j][k] *x[k]
                res /= float(U[j][j])
                x[j] = res
                j-=1
        else:
            return error
        return str(x)

    def all(self):
        text = ''
        text += 'Crout Trivial L1U:\n'
        text += '\n' + self.croutTrivialL1U() + '\n\n'
        text += 'Crout Parcial L1U:\n'
        text += '\n' + self.croutParcialL1U() + '\n\n'
        text += 'Crout Trivial LU1:\n'
        text += '\n' + self.croutTrivialLU1() + '\n\n'
        text += 'Crout Parcial LU1:\n'
        text += '\n' + self.croutParcialLU1() + '\n\n'
        text += 'Cholesky por Filas:\n'
        text += '\n' + self.choleskyPorFilas() + '\n\n'
        text += 'Cholesky por Columnas:\n'
        text += '\n' + self.choleskyPorColumnas() + '\n\n'
        return text
