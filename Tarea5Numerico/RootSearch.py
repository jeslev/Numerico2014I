from math import log, ceil
import math
import copy

class RootSearch():
    
    def __init__(self):
        self.ns = vars(math).copy()
        self.ns['__builtins__'] = None
    
    def f(self, q ,str_function):
        new_fun = ''
        new_fun = copy.deepcopy(str_function)
        new_fun = new_fun.replace('x',str(q))
        new_fun = new_fun.replace('^','**')
        new_fun = new_fun.replace('abs','fabs')    
        return eval(new_fun,self.ns)
    
    def rootsearch(self, s, a, b, dx):
        x1 = a
        f1 = self.f(x1,s)
        x2 = a+dx
        f2 = self.f(x2,s)
        while f1*f2>0.0:
            if x1>=b: 
                return None, None
            x1 = x2
            f1 = f2
            x2 = x1+dx
            f2 = self.f(x2,s)
        else:
            return x1, x2
