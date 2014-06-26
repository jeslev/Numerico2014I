from math import log, ceil
import math
import copy
from RootSearch import *

class Secante:
 
    def __init__(self,s,a,b):
        self.s = s
        self.resumen_res = ''
        #las siguientes 2 lineas son para usar el string como funcion
        self.ns = vars(math).copy()
        self.ns['__builtins__'] = None
        self.txt = ''
        self.txt2 = ''
        self.sep = '-------------------------------------------------------------------------------------------------------------------\n'
        dx = 0.1
        if a==0.0 and b==0.0:
            a = -40.0
            b = 40.0    
        r = RootSearch()
        while 1:
            x1, x2 = r.rootsearch(s,a,b,dx)
            if x1!=None:
                a = x2
                root = self.secante(s,x1,x2,1)
                if root != None:
                    self.resumen_res+='x = '+'{:7.7f}\n'.format(root)
            else:
                break
        
    
    def getmyTxt(self):
        if len(self.resumen_res) > 1:
            self.txt2 +='\n\nRESUMEN - LAS RAICES SON:\n'+self.resumen_res+'\n'
        return self.txt2
        
    #cambiamos todas las 'x' por el valor 'q' pasado por la funcion
    def f(self, q,str_function):
        new_fun = ''
        new_fun = copy.deepcopy(str_function)
        new_fun = new_fun.replace('x','('+str(q)+')')
        new_fun = new_fun.replace('^','**')    
        return eval(new_fun,self.ns)
     
     
    def secante(self, s,x1, x2, switch = 0, epsilon = 1.0e-5):
        f1 = self.f(x1, s)
        if f1 == 0.0:
            self.txt+='\nRpta: '+str(x1)+'\n'
            self.txt+='Y un error de 0.0\n'+self.sep
            self.txt2+=self.txt+'\n\n\n'
            self.txt = ''
            return x1
        f2 = self.f(x2, s)
        if f2 == 0.0:
            self.txt+='\nRpta: '+str(x2)+'\n'
            self.txt+='Y un error de 0.0\n'+self.sep
            self.txt2+=self.txt+'\n\n\n'
            self.txt = ''
            return x2
        if f1*f2>0.0:
            self.txt = "Error multiplicacion positiva de 2 funciones\n\n"
            self.txt2+=self.txt+'\n\n\n'
            self.txt = '' 
            return None
        self.txt+=self.sep+' k\t\tIntervarlo [a_k, b_k]\t\t\t\tu_k\t\t\t\tf(u_k)\t\t\tError\n'+self.sep
        n = 200
        it = 0
        while n>0:
            it+=1
            f1 = self.f(x1, s)
            f2 = self.f(x2, s)
            x3 = x2 - ( (f2*(x2-x1))/(f2-f1) )
            f3 = self.f(x3,s)
            if it<999:
                self.txt+= str(it)+'\t\t[ '+'{:7.7f}'.format(x1)+','' {:7.7f}'.format(x2)+' ]' + '\t\t{:7.7f}'.format(x3)+'\t\t{:7.7f}'.format(f3)+'\t\t'+'{:7.13f}'.format(abs(x3-x2))+'\n'
            else:
                self.txt+= str(it)+'\t[ '+'{:7.7f}'.format(x1)+','' {:7.7f}'.format(x2)+' ]' + '\t\t{:7.7f}'.format(x3)+'\t\t{:7.7f}'.format(f3)+'\t\t'+'{:7.13f}'.format(abs(x3-x2))+'\n'
            if math.fabs(x3-x2)<epsilon:
                if math.fabs(x3)<epsilon*10:
                    self.txt=''
                    return None
                else:
                    self.txt+='\nRpta: '+str(x3)+'\n'
                    self.txt+='Y un error de '+'{:7.13f}'.format(abs(x3-x2))+'\n'+self.sep
                    self.txt2+=self.txt+'\n\n\n'
                    self.txt = ''
                    return x3
            else:
                x1 = copy.deepcopy(x2)
                x2 = copy.deepcopy(x3)
            n-=1
        return x2
