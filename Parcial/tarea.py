import sys
from Tkinter import *
from ConditionNumber import *
from Gauss import *
from Solver import *
from parletreid import *
from aasen2 import *
from HouseHolder import *
import tkMessageBox
import os

mGui = Tk()
w = mGui.winfo_screenwidth()
h = mGui.winfo_screenheight()

matrizA = []
matrizB = []
dim = 0
n = 0
m = 0

def mabout():
    texto = 'Examen Parcial\nAnalisis Numerico\n2014-1'
    tkMessageBox.showinfo('Que es esto?', texto)
    
def creditos():
    texto = 'Jesus Lovon Melgarejo\nMaritza Lapa Romero\nJason Martinez Vera\nGiovanny Mondragon\nAlonso Guillen Vera'
    tkMessageBox.showinfo('Desarrollado por:', texto)


def readMatrixA():
    global dim
    global m
    global n
    global matrizA
    matrizA = []
    f=open("matriz.txt",'r+')
    dim = 0
    while(1):
        line = f.readline()
        if not line:
            break
        dim = dim+1
        numrow = line.split()
        ROW = []
        cnt = 0
        for num in numrow:
            ROW.append(float(num))
            cnt+=1
        n = cnt
        matrizA.append(ROW)    
    m = dim
    return

def readMatrixB():
    global b
    b = []
    f = open("matrizB.txt", 'r+')
    line = f.readline()
    if not line:
        return
    rows = line.split()
    for num in rows:
        matrizB.append(float(num))
    return

def getMatrixAfromText():
    os.system("gedit matriz.txt")
    readMatrixA()

def getMatrixBfromText():
    os.system("gedit matrizB.txt")
    readMatrixB()

def callConditionNumber():
    os.system("python sistema.py")
    #ConditionNumber(matrizA, dim)

def solveSystem():
    mGuiSolve = Toplevel();
    mGuiSolve.geometry('500x700+200+200');
    mGuiSolve.title('Soluciones')
    text = Text(mGuiSolve)

    txt = ''
    A = matrizA[:]
    b = matrizB[:]
    N = dim
    gauss = Gauss(A,b,N)
    txt += gauss.all()
    
    A = matrizA[:]
    b = matrizB[:]
    N = dim
    
    solucion = Solver(A, b, N)
    txt += solucion.all()

    A = matrizA[:]
    b = matrizB[:]
    N = dim
    parlet =  parletreid(A, b, N)
    txt += str(parlet)
    
    A = matrizA[:]
    b = matrizB[:]
    N = dim
    aasentxt =  aasen(A, b, N)
    txt += str(aasentxt)
    
    A = matrizA[:]
    b = matrizB[:]
    N = dim
    hh =  HouseHolder(A, n, m, b)
    txt += str(hh.all())

    text.insert(INSERT, txt)
    text.insert(END, '....')
    text.place(x = 20, y = 20, width = 460, height = 660)

def main():
    #mGui = Tk()
    mGui.geometry('500x250+'+ str(w/2 - 250) + '+' + str(h/2 - 200))
    mGui.title('Mecanica mediante Sistemas de Ecuaciones Lineales')
    label = Label(mGui, text = 'Ax = b', font = ('Helvetica', 25)).place(x = 55, y = 15)
    
    imagenL = PhotoImage(file='logo.png')
    lblImagen = Label(mGui, image = imagenL).place(x = 20, y = 70)

    readMatrixA()
    readMatrixB()

    mbotonMatrizA = Button(mGui, text = 'Ingrese la matriz A', 
            command = getMatrixAfromText).place(x=240,y=20, height = '30', width ='200')

    mbotonMatrizB = Button(mGui, text = 'Ingrese b', 
            command = getMatrixBfromText).place(x=240,y=80, height = '30', width ='200')

    mbotonConditionNumber = Button(mGui, text = 'Resolver Sistema de Ecuaciones', 
            command = solveSystem).place(x=240,y=140, height = '30', width = '200')
    
    mbotonDemo = Button(mGui, text = 'Demo', 
            command = callConditionNumber).place(x=240,y=200, height = '30', width = '200')

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
