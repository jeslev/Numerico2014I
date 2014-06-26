import sys
from Tkinter import *
import tkMessageBox
import struct
from FloatsClass import FloatsClass
from ErrorCalc import ErrorCal

mGui = Tk()
mynum = DoubleVar()

def getEpsilonMachine():
    eps = float(1)
    while float(1)+ eps != float(1):
        last_eps = eps
        eps = eps/float(2)
    res = last_eps
    Label(mGui, text = res,fg='blue').place(x=200,y=65)

def getLongPalabra():
    long_palabra = struct.calcsize('P') * 8 
    texto = str(long_palabra) + ' bits'
    Label(mGui, text = texto,fg='blue').place(x=200,y=25)

def getErrorNum():
    errors = ErrorCal(mynum.get())
    relerr, abserr, absexp = errors.getAbsoluteError()
    #print abserr,absexp
    texto = 'Error Absoluto:\n'+abserr+' x10^' + str(absexp)+'\nError relativo:\n'+relerr+' x10^' + str(absexp)
    tkMessageBox.showinfo('Resultado', texto)

def getSetFloat():
    #Abre nueva ventana para ingresar parametros para armar conjunto de numeros
    sets = FloatsClass()
    return

def mabout():
    texto = 'Primer trabajo\nAnalisis Numerico\n2014-1'
    tkMessageBox.showinfo('Que es esto?', texto)
    
def creditos():
    texto = 'Jesus Enrique Lovon Melgarejo\nMaritza Lapa Romero\nEdgar Huaranga Junco\nGiovanny Mondragon '
    tkMessageBox.showinfo('Desarrollado por:', texto)

def main():
    #mGui = Tk()
    mGui.geometry('450x200+200+200')
    mGui.title('Tarea 1 Calculo Numerico')
    
    mbotonLongPalabra = Button(mGui, text = 'Longitud de Palabra',command = getLongPalabra).place(x=20,y=20)
    mbotonEpsilonMachine = Button(mGui, text = 'Epsilon de Maquina',command = getEpsilonMachine).place(x=20,y=60)
    
    mtextNum = Entry(mGui, textvariable = mynum).place(x=20,y=110)
    mbotonGetError = Button(mGui, text = 'Calcular error', command = getErrorNum).place(x=200, y=110)
    #print "El beta (base) es ",betha)
    
    mbotonSetnum = Button(mGui, text = 'Calcular numeros maquina', command = getSetFloat).place(x=20, y = 150)
    
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
