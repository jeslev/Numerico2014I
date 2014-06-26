import sys
from Tkinter import *
from Factorizar import *
from Solver import *
from Gauss import *
import tkMessageBox
import os

mGui = Tk()
mynum = DoubleVar()
matrizA = []
dim = 0
isSymetric = True
isRegular = False
isSquare = False

def mabout():
    texto = '2da Tarea\nAnalisis Numerico\n2014-1'
    tkMessageBox.showinfo('Que es esto?', texto)
    
def creditos():
    texto = 'Jesus Lovon Melgarejo\nMaritza Lapa Romero\nJason Martinez Vera\nGiovanny Mondragon '
    tkMessageBox.showinfo('Desarrollado por:', texto)

def getMatrixfromText():
    os.system("gedit matriz.txt")

def readMatrix():
    global dim
    f=open("matriz.txt",'r+')
    dim = 0
    while(1):
        line = f.readline()
        if not line:
            break
        dim = dim+1
        numrow = line.split()
        ROW = []
        for num in numrow:
            ROW.append(float(num))
        matrizA.append(ROW)            
    return


def det(A,b):
    determinante = 0.0
    c=0
    if b==2 :
        return A[0][0]*A[1][1]-A[1][0]*A[0][1]
    else:
        for j in range(b):
            M= [ [ 0 for i in range(b-1) ] for h in range(b-1) ]
            for k in range(1,b):
                c=0
                for l in range(b):
                    if l!=j:
                        M[k-1][c]=A[k][l] 
                        c+=1

            aux=pow(-1,2+j)*A[0][j]*det(M,b-1)
            determinante+=aux
            
    return determinante 

def showStatus():
    statussq = 'Matriz cuadrada? ' + str(isSquare)
    statusim = 'Matriz simetrica? '+ str(isSymetric)
    statusreg = ' Matriz regular? '+str(isRegular) 
    Label(mGui, text=statussq, fg='blue').place(x=180,y=60)
    Label(mGui, text=statusim, fg='blue').place(x=180,y=100)
    Label(mGui, text=statusreg, fg='blue').place(x=180,y=140)

def checkMatrix():
    global isSymetric, isRegular, isSquare
    readMatrix()
    ''' Revisar si es cuadrada '''
    MaxR = 0
    for row in matrizA:
        MaxR = max(MaxR, len(row))
    if MaxR == dim:
        isSquare = True
    if not isSquare:
        isSymetric = False
        showStatus()
        return
    ''' Revisar si es simetrica '''
    for i in range(dim):
        for j in range(dim):
            if matrizA[i][j] != matrizA[j][i]:
                isSymetric = False
    ''' Revisar si es regular '''
    if det(matrizA,dim)==0:
        isRegular=False
    else: isRegular=True
    showStatus()
    #print isSymetric, isRegular
    
def factorizeMatrix():
    if(isRegular and isSquare):
        fact = Factorizar(matrizA,dim,isSymetric)
    if not isRegular:
        tkMessageBox.showinfo('AVISO!', 'No es una matriz regular!')
        return
    #if not isSymetric:
    #    tkMessageBox.showinfo('AVISO!', 'No es una matriz simetrica!')
    
def solveMatrix():
    if(isRegular and isSquare):
         gauss = Gauss(matrizA,dim)
    if not isRegular:
        tkMessageBox.showinfo('AVISO!', 'No es una matriz regular!')
        return
    return


def solveMatrix2():
    if(isRegular and isSquare):
         gauss = Solver(matrizA,dim)
    if not isRegular:
        tkMessageBox.showinfo('AVISO!', 'No es una matriz regular!')
        return
    return

def main():
    #mGui = Tk()
    mGui.geometry('450x200+200+200')
    mGui.title('Sistema de ecuaciones lineales')

    mbotonMatriz = Button(mGui, text = 'Ingrese la matriz', command = getMatrixfromText).place(x=20,y=20)
    mbotonCheck = Button(mGui,text = 'Revisar matriz', command = checkMatrix ).place(x=20,y=60)    
    
    mbotonFactorizar = Button(mGui, text = 'Factorizar Matriz', command = factorizeMatrix).place(x=20, y = 100)
    mbotonResolver = Button(mGui, text = 'Resolver por Gauss', command = solveMatrix).place(x=20,y=140)
    mbotonResolver2 = Button(mGui, text = 'Resolver sistemas', command = solveMatrix2).place(x=20,y=180)
    
    #MENU
    menubar = Menu(mGui)
    filemenu = Menu(menubar,tearoff=0)
    filemenu.add_command(label='About', command =mabout)
    filemenu.add_command(label='Creditos',command = creditos)
    menubar.add_cascade(labe= 'Help',menu=filemenu)
    mGui.config(menu = menubar)
        
    mGui.mainloop()

if __name__ == "__main__":
    main()
