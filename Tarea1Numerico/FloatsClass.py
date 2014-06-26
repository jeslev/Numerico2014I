import sys
from Tkinter import *
import tkMessageBox
import struct
import string
class FloatsClass:    

    def __init__(self):
        #default para MARC-32
        self.betha = 2
        self.mantisa = 23
        self.expU = 2
        self.expL = -2
        self.graphics()
        
    def graphics(self):
        global mGui, varbetha,varmant,varexpl,varexpu,varbin,varerr
        mGui = Toplevel()
        varbetha = IntVar()
        varmant = IntVar()
        varexpl = IntVar()
        varexpu = IntVar()
        varbin = StringVar()
        varerr = StringVar()
        mGui.geometry('700x300+450+300')
        mGui.title('Ingrese datos para armar el conjunto')
        mlabel1 = Label(mGui, text= 'Numero betha (base)').place(x=20,y=20)  
        mbetha = Entry(mGui, textvariable = varbetha).place(x=200,y=20)
        mlabel2 = Label(mGui, text= 'Tamano mantisa (t)').place(x=20,y=60)  
        mmantisa = Entry(mGui, textvariable = varmant).place(x=200,y=60)
        mlabel3 = Label(mGui, text= 'Minima potencia (L)').place(x=20,y=100)  
        mlowexp = Entry(mGui, textvariable = varexpl).place(x=200,y=100)
        mlabel4 = Label(mGui, text= 'Maxima potencia (U)').place(x=20,y=140)  
        mupexp = Entry(mGui, textvariable = varexpu).place(x=200,y=140)
        mbuton = Button(mGui, text = 'Calcular numeros',command = self.getFloats).place(x=20, y = 180)
        mbuton2 = Button(mGui, text = 'Calcular cantidad de numeros',command = self.getTotalSet).place(x=200, y = 180)
        mlabel5 = Label(mGui, text= 'Numero de forma (a/b)').place(x=20,y=220)  
        mbin = Entry(mGui, textvariable = varbin).place(x=200,y=220)
        mbuton3 = Button(mGui, text = 'Calcular binario',command = self.getBinario).place(x=320, y = 220)
        mlabel6 = Label(mGui, text= 'Buscar error (a/b)').place(x=20,y=260)
        merror = Entry(mGui, textvariable = varerr).place(x=200,y=260)
        mbuton4 = Button(mGui, text = 'Encontrar error(a/b)',command = self.getError).place(x=320, y = 260)
        #mGui.mainloop()          
       
    def mult_posi(self,num,fi):
        cont=self.expL
        den=pow(self.betha,self.expU+self.mantisa)
        total=''        
        while cont <= self.expU :
            cad2=str(num)+"/" +str(den)+ " "
            total +=  cad2
            cont+=1
            num*=self.betha
        fi.write(total+"\n")

    def mult_nega(self,num,fi):
        cont=self.expL
        den=pow(self.betha,self.expU+self.mantisa)
        total=''              
        while cont <= self.expU :
            cad2="-"+str(num)+"/" +str(den)+" "
            total = cad2 + total
            cont+=1
            num*=self.betha
        fi.write(total+"\n")


    def gene_posi (self,fi):
        num=pow(self.betha,self.mantisa-1)
        den=pow(self.betha,self.mantisa)
        while num != den: 
            self.mult_posi(num,fi)
            num+=1



    def gene_nega(self,fi):
        num=pow(self.betha,self.mantisa-1)
        den=pow(self.betha,self.mantisa)
        num2=den-1
        while num2 != num-1: 
            self.mult_nega(num2,fi)
            num2-=1    


    def leer(self,fi):
        total=''
        for line in fi:
            total+=line
        return total


    def getTotalSet(self):
        self.betha = varbetha.get()
        self.mantisa = varmant.get()
        self.expU = varexpu.get()
        self.expL = varexpl.get()
        total = (self.betha -1)*(pow(self.betha, self.mantisa-1))*(self.expU - self.expL +1)
        total = total*2 +1
        tkMessageBox.showinfo('Total de elementos', 'Hay en total ' + str(total) + ' numeros maquina')

    def getFloats(self):
        #calcula el conjunto
        #muestra en un archivo de texto
        self.betha = varbetha.get()
        self.mantisa = varmant.get()
        self.expU = varexpu.get()
        self.expL = varexpl.get()
        #calcula el conjunto
        fi=open("numerosmaqui.txt","w")
        self.gene_nega(fi)
        fi.write("0\n")
        self.gene_posi(fi)
        fi.close()
        
        fi=open("numerosmaqui.txt","r")
        cade=self.leer(fi)
        fi.close()    
        tkMessageBox.showinfo('AVISO!', 'Numeros generados, revisar archivo!')
        #muestra en un archivo de texto
        
    def bin_ente (self,N): 
        cade="{0:b}".format(N)
        return cade

    def bin_frac(self,D,man,base):
        b=0.00
        cade=''
        i=0    
        while i!=man:
            D=float(base)*D
            b=int(float(D)) 
            cade+=str(b)        
            if D>=float(1):            
                ente=int(D)
                D=float(D-ente)        
            i+=1
        return cade


    def copiar(self,str1,ini,posi):
        i=ini
        cade=''
        while i!=posi:
            cade+=str(str1[i])
            i+=1
        return cade
        
        
    def getBinario(self):
        bas= varbetha.get()#base
        t=varmant.get() #tamano mantisa
        exp=varexpu.get() - varexpl.get()#tamano pa lo exponentes
        sgmant='1'
        sgexpo='1'
        N= varbin.get()
        exponente=''
        represent=''
        divi=N.find("/")

        a= self.copiar(N,0,divi)
        b= self.copiar(N,divi+1,N.__len__())

        numero=float(int(a)/float(b))

        if numero>=float(0):
            sgmant='0'

        ente=abs(int(float(numero)))
        deci=abs(float(abs(float(numero))-ente)) 
        if ente>0:
            sgexpo='0'
            cade1=self.bin_ente(ente)
            tent=cade1.__len__()
            bexpo=self.bin_ente(tent-1)
            for j in range(exp-bexpo.__len__()-1):
                exponente+='0'
            exponente+=bexpo
            cade2 =self.bin_frac(deci,t-tent+1,bas) #trans de la parte binaria
            cad3 = ''
            mant = ''
            cad3 = cade1+cade2
            mant = cad3[1:]
            represent=sgmant+" "+sgexpo+"\n"+exponente+"\n"+mant

        else:
            cade2 =self.bin_frac(deci,t+1,bas)
            pri1=cade2.find("1")
            segexpo='1'
            if pri1 != 0:
                cade2=self.bin_frac(deci,t+pri1+1,bas)
                sgexpo='1'
                bexpo=self.bin_ente(pri1+1)
                for j in range(exp-bexpo.__len__()-1):
                    exponente+='0'
                exponente+=bexpo
            else: 
                exponente = '1'
                cad3=''
                for j in range(exp-1):
                    cad3+='0'
                exponente=cad3+exponente
            cad1=''
            for j in range(t):    
                cad1+=cade2[pri1+j+1]
            
            represent=sgmant+" "+sgexpo+" "+exponente+" "+cad1

        tkMessageBox.showinfo('En binario', represent)


    def getError(self):
        A= varerr.get()
        p=A.find('/',0)
        a=int(A[0:p])
        f=open("numerosmaqui.txt",'r+')
        answ=False
        difMin=100000000
        while(True):
                line=f.readline()
                if not line: break
                espa=0
                div=line.find('/')
                denom=int(line[div+1:line.find(' ',1)])
                while(True):
                        numtxt=line[espa:div]
                        #print numtxt
                        if(numtxt[0:1]=='-'):
                                numint=-int(numtxt[1:len(numtxt)])
                        else:
                                numint=int(numtxt)
                        dif=abs(a-numint)
                        if(dif<difMin):difMin=dif
                        if(dif==0):
                                answ=True
                        espa=line.find(' ',espa+1)+1
                        div=line.find('/',div+1)
                        if(espa==0 or div==-1): break
        f.close()
        msg = ""              
        if(answ): msg = "Encontrado\nNo hay error"
        else:
                msg = "No esta en el archivo\ndiferencia minima: "+str(float(difMin)/float(denom))
        tkMessageBox.showinfo('Busqueda', msg)
