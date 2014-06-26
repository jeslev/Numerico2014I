import string
from  math import *

class Givens:
    
    def __init__(self,A,m,n,B):
        self.A = A
        self.m = m
        self.n = n
        self.B = b
        self.a=[ [ 0 for i in range(m+1) ] for j in range(n+1) ]
        self.b=[ 0 for i in range(m+1)]

    def paso(self,A):
        a=[ [ 0 for i in range(m+1) ] for j in range(n+2) ]
        for i in range (m):
            for j in range(n):
                a[i+1][j+1]=A[i][j]
        return a

    def paso2(self,B):
        b=[ 0 for i in range(m+1) ] 
        for i in range (m):
                b[i+1]=B[i]
        return b



    ##########
    def givens2(self,a,b):
        t=0.0
        s=0.0
        c=0.0
        aux=0.0 
        n = self.n
        m = self.m            

     ###     EMPIEZA  ################
        for i in range (1,n+1):
            for  k in range (i+1,m+1):
                if ( ( float(1)+a[k][i] ) != float(1) ):
                    if( abs(a[k][i]>=a[i][i]) ):
                        t=a[i][i]/a[k][i]
                        s=float(1)/sqrt(1.0+t*t)
                        c=s*t
                    else: 
                        t=a[k][i]/a[i][i]
                        c=float(1)/sqrt(1.0+t*t)
                        s=c*t
                    a[i][i]=c*a[i][i]+s*a[k][i]

                    for j in range (i+1,n+1):
                        aux = c*a[i][j] + s*a[k][j]
                        a[k][j] = (-s*a[i][j])+c*a[k][j]
                        a[i][j]=aux

                    aux=c*b[i]+s*b[k]
                    b[k]=(-s*b[i])+c*b[k]
                    b[i]=aux
        
    ###fin
        return a,b
        
    def calcular(self):
        a=paso(self.A)
        b=paso2(self.B)

        n = self.n
        m = self.m
        a,b = givens2(a,b)
        x = []
        for i in range(n):
	        x.append(0.0)

        ####resolucion Rx=b
        x[n-1]=b[n]/a[n][n]
        for i in range (n-1,0,-1):
            suma=0.0
            for k in range(i+1,n+1):
                suma=suma+a[i][k]*x[k-1]
            x[i-1]=(b[i]-suma)/a[i][i]

        ###residuos cuadrado
        s=0.0
        for i in range (n+1,m+1):
            s=s+b[i]*b[i]

        txt='Givens'
        txt+='\n' + str(x) + '\n\n'
        txt+='Suma de residuos al cuadrado'
        txt+='\n' + str(s) + '\n\n'


        print txt



