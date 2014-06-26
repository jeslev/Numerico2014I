import math
import copy
import numpy
from RootSearch import *
class PicardJacobi:
 
    def __init__(self,f,x,c):
        self.txt = ''
        self.txt2 = ''
        self.fs = f
        self.x = x
        self.c = c
        self.sep = '-------------------------------------------------------------------------------------------------------\n'
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
                self.pjacobi(f,x,c)
                print '\n\n'
                print '\n\n'
        else:
            self.pjacobi(f,x,c)
          
    
    def getmyTxt(self):
        return self.txt2
        
    def jacobian(self,f,x,c):
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
                jac[j][i] *= c[j]
                if j==i: jac[j][i]+=1 
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

    
        
    def pjacobi(self, fs,x,c, epsilon = 1.0e-5):
        ini_x = copy.deepcopy(x)
        self.txt += '\n\n'+self.sep+'\t\t\tX\t\t\t\t\t\t\tError\n'+self.sep+'\n'
        jact = 1.0
        for i in range(30):
            n = len(x)
            f0,f1 = self.jacobian(fs,x,c)
            jac = numpy.linalg.norm(f0)
            xold = copy.deepcopy(x)
            for j in range(n):
                x[j] = x[j] + c[j]*self.f(x,fs[j])
            errrel = jact*( math.sqrt(self.dot(xold,xold)) - math.sqrt(self.dot(x,x)))
            jact *=jac
            
            x_str = '( '
            for i in range(len(x)):
                if i != 0.0:
                    x_str+=(', ')
                x_str+='{:6.10f}'.format(x[i])
            x_str+=' )'
            self.txt += str(x_str) + '\t\t' + str(errrel)+'\n'
            if math.fabs(errrel) > 1.5383145462e+13:
                self.txt = ''
                #self.txt = '\n'+self.sep+'Diverge con X_0 = '+str(ini_x)+'\n'+self.sep+'\n'
                self.txt2 += self.txt
                self.txt = ''
                return 'Resultado' 
            if math.fabs(errrel) < epsilon:
                self.txt+='\nRpta: La solucion para X es: '+str(x)+'\n'
                self.txt+='Y el error es : ''{:6.10f}'.format(errrel)+'\n'+self.sep+'\n\n'
                self.txt2+=self. txt
                self.txt = ''
                print x
                print 'Resultado'
                return 'Resultado'
        self.txt = ''
        #self.txt += '\n'+self.sep+'Diverge con X_0 = '+str(ini_x)+'\n'+self.sep+'\n'
        self.txt2 += self.txt
        self.txt = ''
        print x
        print 'No llega a converger'
