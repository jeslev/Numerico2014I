from math import log, ceil
import math
import copy
from RootSearch import *

class RegulaFalsi:
 
    def __init__(self,s,a,b):
        self.s = s
        self.resumen_res = ''
        #las siguientes 2 lineas son para usar el string como funcion
        self.ns = vars(math).copy()
        self.ns['__builtins__'] = None
        self.txt = ''
        self.txt2 = ''
        self.sep = '--------------------------------------------------------------------------------------------------------------------\n'
        dx = 0.01
        if a==0.0 and b==0.0:
            a = -40.0
            b = 40.0
        r = RootSearch()
        cnt = 0
        while 1:
            x1, x2 = r.rootsearch(s,a,b,dx)
            if x1!=None:
                a = x2
                root = self.falsi(s,x1,x2,1)
                if root != None:
                    self.resumen_res+='x = '+'{:7.7f}\n'.format(root)
            else:
                print '\n'
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
     
    def falsi(self, s,x1, x2, switch = 0, epsilon = 1.0e-5):
        f1 = self.f(x1, s)
        error = 0.0
        ini_x1 = x1
        ini_x2 = x2
        if f1 == 0.0:
            self.txt+='\nRpta: x = '+str(x1)+'\n'
            self.txt+='Y un error de 0.0\n'+self.sep
            self.txt2+=self.txt+'\n\n\n'
            self.txt = ''
            return x1
        f2 = self.f(x2, s)
        if f2 == 0.0:
            self.txt+='\nRpta: x = '+str(x2)+'\n'
            self.txt+='Y un error de 0.0\n'+self.sep
            self.txt2+=self.txt+'\n\n\n'
            self.txt = ''
            return x2
        if f1*f2>0.0:
            self.txt = "Error multiplicacion positiva de 2 funciones"
            self.txt2+=self.txt+'\n\n\n'
            self.txt = '' 
            return -1
        self.txt+=self.sep+' k\t\tIntervalo [a_k, b_k]\t\t\t\tu_k\t\t\tf(a_k)\t\t\tf(b_k)\t\t\tf(u_k))\t\t\terror\n'+self.sep
        n = 50
        it = 0
        xold=0.0
        while n>0:
            it+=1
            x3 = (x1*f2-x2*f1)/(f2-f1)
            f3 = self.f(x3, s)
            if(it<1000):
                self.txt+= str(it)+'\t\t[ '+'{:7.7f}'.format(x1)+','' {:7.7f}'.format(x2)+' ]' + '\t\t\t{:7.7f}'.format(x3)+'\t\t{:7.7f}'.format(f1)+'\t\t{:7.7f}'.format(f2)+'\t\t{:7.7f}'.format(f3)+'\t\t{:7.13f}'.format(math.fabs(xold-x3))+'\n'
            else:
                self.txt+= str(it)+'\t[ '+'{:7.7f}'.format(x1)+','' {:7.7f}'.format(x2)+' ]' + '\t\t\t{:7.7f}'.format(x3)+'\t\t{:7.7f}'.format(f1)+'\t\t{:7.7f}'.format(f2)+'\t\t{:7.7f}'.format(f3)+'\t\t{:7.13f}'.format(math.fabs(xold-x3))+'\n'


            if (switch == 1) and (math.fabs(f3)>math.fabs(f1)) and (math.fabs(f3)>math.fabs(f2)):
                #self.txt = '\nError:\nNo se encuentra la posible raiz en el rango de [ '+str(ini_x1)+', '+str(ini_x2)+' ], si existiese es debido a que la funcion en dicho intervalo no cumple los requerimientos para Regula Falsi\n\n'+self.sep
                self.txt=self.sep+str(x3)+' Falsa aproximacion de raiz\n'+self.sep
                self.txt2+=self.txt+'\n\n\n'
                self.txt=''
                return None
            if f3==0.0:
                self.txt+='\nRpta: x = '+str(x3)+'\n'
                self.txt+='Y un error de '+'{:7.13f}'.format(math.fabs(xold-x3))+'\n'+self.sep
                self.txt2+=self.txt+'\n\n\n'
                self.txt = ''
                return x3
           
            if f2*f3 < 0.0:
                x1 = x3
                f1 = f3
            else:
                x2 = x3
                f2 = f3
            error = x3-xold
            xold = x3
            if abs(f3)<epsilon:
                break
        self.txt+='\nRpta: x = '+str(x3)+'\n'
        self.txt+='Y un error de '+'{:7.13f}'.format(math.fabs(xold-x3))+'\n'+self.sep
        self.txt2+=self.txt+'\n\n\n'  
        self.txt = ''        
        return x3
