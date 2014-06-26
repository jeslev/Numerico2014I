import sys
import tkMessageBox
from Tkinter import *
#from Tkinter import messagebox
def mhello():
    #pass
    Label(mGui,text = ment.get(),fg='red').pack()
    return
    
def mabout():
    tkMessageBox.showwarning    ("About","This is my About")
    return 
    
mGui = Tk()
ment = StringVar()
mGui.geometry('450x450+200+200')
mGui.title('My app :)')

#mLabel = Label(text = 'My Label',fg='red').place(x=225,y=225,sticky=W) //sticky alinea W west, E east
#mLabel = Label(mGui,text = 'My Label',fg='red').grid(row=0,column=0)

mLabel = Label(mGui,text = 'My Label',fg='red').pack()
mbutton = Button(mGui, text= 'OK',command = mhello).pack()
#mLabel.pack()

mEntry =  Entry(mGui,textvariable = ment).pack()

#MENU
menubar = Menu(mGui)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label='New', command =mabout)
filemenu.add_command(label='Open')
filemenu.add_command(label='Save as ...')
filemenu.add_command(label='Close')


menubar.add_cascade(labe= 'File',menu=filemenu)
mGui.config(menu = menubar)
mGui.mainloop()
