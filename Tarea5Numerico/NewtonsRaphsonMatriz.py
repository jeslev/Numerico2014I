import math
import copy
from RootSearch import *
class RaphsonMatrix:
 
    def __init__(self,f,x):
        self.txt = ''
        self.txt2 = ''
        self.fs = f
        self.x = x
        self.sep = '------------------------------------------------------------------------------------------------------------------\n'
        #las siguientes 2 lineas son para usar el string como funcion
        self.ns = vars(math).copy()
        self.ns['__builtins__'] = None
        if x == None:
            i = -20
            while i < 20:
                x = []
                for j in range(len(f)):
                    x.append(i+0.5*j)
                i += 0.5
                print i, x
                self.rmatriz(f,x)
                print '\n\n'
                print '\n\n'
        else:
            self.rmatriz(f,x)
          
    
    def getmyTxt(self):
        return self.txt2
        
    def jacobian(self,f,x):
        h = 1.0e-4
        n = len(x)
        jac = [[ 0.0 for i in range(n)] for j in range(n)] 
        f0 = self.ff(f,x)
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = self.ff(f,x)
            x[i] = temp
            for j in range(n):
                jac[j][i] = (f1[j]-f0[j])/h
        return jac,f0
        
    def ff(self,fx,x):
        n = len(x)
        res = []
        for myf in fx:
            p = self.f(x,myf)
            res.append(p)
        return res
        
    #cambiamos todas las 'x' por el valor 'q' pasado por la funcion
    def f(self, q,str_function):
        new_fun = ''
        new_fun = copy.deepcopy(str_function)
        new_fun = new_fun.replace('^','**')
        new_fun = new_fun.replace('abs','fabs')
        for i in range(len(q)):
            new_fun = new_fun.replace('x'+str(i+1),'('+str(q[i])+')')
        return eval(new_fun,self.ns)
     
        
    def dot(self,f1,f2):
        n = len(f1)
        res = 0.0
        for i in range(n):
            res+= (f1[i]*f2[i])
        return res
    
    def lu(self,A):
        diverge = False
        n = len(A)
        p = range( n )
        s = [0] * n
        for i in xrange( n ):
            smax = 0.0
            for j in xrange( n ):
                smax = max( smax, math.fabs( A[i][j] ) )
            s[i] = smax
            print s[i]
        #Gaussian elimination.
        
        for k in xrange( n - 1 ):
            rmax = 0.0
            if diverge == True:
                break
            for i in xrange( k, n ):
                if s[p[i]]==0:
                    diverge = True
                    break
                else:
                    r = math.fabs( A[p[i]][k] / s[p[i]] )
                    if r > rmax:
                        rmax = r
                        j = i

            if diverge == False:
                p[j], p[k] = ( p[k], p[j] )
                for i in xrange( k + 1, n ):
                    xmult = A[p[i]][k] / A[p[k]][k]
                    A[p[i]][k] = xmult
                    for j in xrange( k + 1, n ):
                        A[p[i]][j] = A[p[i]][j] - xmult * A[p[k]][j]
                return A, p
            else:
                return None, None 

    def solve(self,A, p, b ):
        n = len(A)
        x = [0.0 for i in range(n)]

        for k in xrange( n - 1 ):
            for i in xrange( k + 1, n ):
                b[p[i]] = b[p[i]] - A[p[i]][k] * b[p[k]]

        for i in xrange( n - 1, -1, -1 ):
            suma = b[p[i]]
            for j in xrange( i + 1, n ):
                suma = suma - A[p[i]][j] * x[j]
            if A[p[i]][i]==0.0:
                return None
            x[i] = suma / A[p[i]][i]
        return x
    
    
    def maxArray(self, x):
        maxi = 0
        for i in x:
            maxi = max(math.fabs(i),maxi)
        return maxi
        
    def rmatriz(self, f,x, epsilon = 1.0e-5):
        ini_x = copy.deepcopy(x)
        self.txt += '\n\n'+self.sep+'\t\t\tX\t\t\t\t\t\t\tdx\n'+self.sep+'\n'
        for i in range(40):
            jac,f0 = self.jacobian(f,x)
            if math.sqrt(self.dot(f0,f0)/len(x)) < epsilon:
                x_str = '( '
                for i in range(len(x)):
                    if i != 0.0:
                        x_str+=(', ')
                    x_str+='{:6.7f}'.format(x[i])
                x_str+=' )'
                self.txt+='\nRpta: La solucion para X es: '+str(x_str)+'\n'+self.sep+'\n\n'
                self.txt2+=self. txt
                self.txt = ''
                return x
            jac,p = self.lu(jac)
            if jac == None and p == None:
                self.txt = ''
                #self.txt = '\n'+self.sep+'Diverge con X_0 = '+str(ini_x)+'\n'+self.sep+'\n'
                self.txt2 += self.txt
                self.txt = ''
                return x
                
            faux = copy.deepcopy(f0)
            for j in range(len(faux)):
                faux[j] *=-1
            dx = self.solve(jac,p,faux)
            if dx == None:
                self.txt = ''
                #self.txt = '\n'+self.sep+'Diverge con X_0 = '+str(ini_x)+'\n'+self.sep+'\n'
                self.txt2 += self.txt
                self.txt = ''
                return x
            x_str = '( '
            for i in range(len(x)):
                if i != 0.0:
                    x_str+=(', ')
                x_str+='{:6.7f}'.format(x[i])
            x_str+=' )'
            self.txt += str(x_str) + '\t\t' + str(dx)+'\n'
            
            for j in range(len(x)):
                x[j] = x[j]+dx[j]
            if math.sqrt(self.dot(dx,dx)) < epsilon*max(self.maxArray(x),1.0):
                x_str = '( '
                for i in range(len(x)):
                    if i != 0.0:
                        x_str+=(', ')
                    x_str+='{:6.7f}'.format(x[i])
                x_str+=' )' 
                self.txt+='\nRpta: La solucion para X es: '+str(x_str)+'\n'+self.sep+'\n\n'
                self.txt2+=self. txt
                self.txt = ''
                return x
        self.txt = ''
        #self.txt = '\n'+self.sep+'Diverge con X_0 = '+str(ini_x)+'\n'+self.sep+'\n'
        self.txt2 += self.txt
        self.txt = ''
