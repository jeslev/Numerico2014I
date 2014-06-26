import math
import copy
from RootSearch import *

class PuntoFijoAitken:
 
    def __init__(self,s,a,b):
        
        self.s = s
        self.resumen_res = ''
        #las siguientes 2 lineas son para usar el string como funcion
        self.ns = vars(math).copy()
        self.ns['__builtins__'] = None
        self.txt = ''
        self.txt2 = ''
        self.sep = '-------------------------------------------------------------------------------------------------------\n'
        dx = 0.01
        if a==0.0 and b==0.0:
            a = -40.0
            b = 40.0
        r = RootSearch()
        while 1:
            x1, x2 = r.rootsearch(s,a,b,dx)
            if x1!=None:
                a = x2
                x = 0.5*(x1+x2)
                aa = -1.0/(self.df(x,s))
                root = self.pfijoAitken(s,x1,x2,aa)
                if root != None:
                    self.resumen_res+='x = '+'{:6.7f}\n'.format(root)
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
        new_fun = new_fun.replace('abs','fabs')    
        return eval(new_fun,self.ns)
     
     
    def df(self,x,s):
        h = 1.0e-6
        fxh = self.f(x+h,s)
        fx = self.f(x,s)
        d = (fxh - fx)/h
        return d
        
    def pfijoAitken(self, s,x0,x1, aa,switch = 0, epsilon = 1.0e-5):
        x = (x0+x1)*0.5
        ini_x = x
        f1 = self.f(x,s)
        if f1 == 0.0:
            self.txt+='\nRpta: x = '+str(x)+' con x_0 = '+str(ini_x)+'\n'
            self.txt+='Y un error de 0.0 \n'+self.sep
            self.txt2+=self.txt+'\n\n\n'
            self.txt = ''
            return x
        
        self.txt+=self.sep+' k\t\t\tx_k\t\t\t\tfx_k\t\t\t\tError\n'+self.sep
        k = 0
        it =0
        error = math.fabs(x0-x1)
        while k < 60:
            it+=1
            x2, x1, x0 = ( x1, x0, x )
            fx = self.f(x,s)
            p1 = x  + aa * fx
            fp1 = self.f(p1,s)
            p2 = p1 + aa * fp1
            d =  p2 - 2 * p1 + x 
            xold = x
            self.txt+= "%2d %18.11e %18.11e %18.11e\n" % ( it, x,self.f(x,s),math.fabs(error) )
            if d==0:
                self.txt+='\nRpta: x = '+str(x)+' con x_0 = '+str(ini_x)+'\n'
                self.txt+='Y un error de '+str(math.fabs(error))+'\n'+self.sep
                #self.txt+='Diverge la solucion\n'
                self.txt2+=self.txt+'\n\n\n'
                self.txt = ''
                return p2
            else:
                x = x - ( ( p1 - x )**2 ) / d
            
            
            if xold==0:
                error = x
            else:
                error = (x-xold)/xold 
            
            #if error<epsilon:
            #    self.txt+='Diverge la solucion\n'
            #    self.txt2+=self.txt+'\n\n\n'
            #    self.txt = ''
            #    return x
                
            if math.fabs(x) > 1.0e10:
                self.txt+='Diverge\n'
                self.txt2+=self.txt+'\n\n\n'
                self.txt = ''
                return None
            
            k+=1
        self.txt=self.sep+'No converge con x_0 = '+str(ini_x)+'\n'+self.sep+'\n\n\n'
        self.txt2+=self.txt+'\n\n\n'
        self.txt = ''
        return None
