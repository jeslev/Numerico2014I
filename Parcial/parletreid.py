def init():
    global A, a ,b, n
    A=[]
    for i in range(n):
        A.append([0]*(n+1))
    for i in range(n):
        for j in range(n):
            A[i][j]=a[i][j]
    for i in range(n):
        A[i][n]=b[i]

def inversa(M,n):
    I=[]
    for i in range (n):
        I.append([0]*(n))
    for i in range (n):
        I[i][i]=1
    mayor=0
    Q=[]
    Q1=[]
    for s in range (n):
        Q.append(0)
        Q1.append(0)
    for i in range (n):
        j=i+1
        if M[i][i]==0:
            p=i+1
            mayor = M[j][i]
            for j in range (i+2,n):
                if(abs(mayor) < abs(M[j][i])):
                    mayor= M[j][i]
                    p = j
            Q=M[i]
            M[i]=M[p]
            M[p]=Q
            Q1=I[i]
            I[i]=I[p]
            I[p]=Q1
        for j in range (0,i):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
            for k in range (n):
                I[j][k] =I[j][k] - (w*I[i][k])
        for j in range (i+1,n):
            w = M[j][i]*(M[i][i])**(-1)
            for k in range (i,n):
                M[j][k] =M[j][k] - (w*M[i][k])
                M[j][i]=0
            for k in range (n):
                I[j][k] =I[j][k] - (w*I[i][k])
    for i in range (n):
        I[i][i]=I[i][i]*(M[i][i])**(-1)
    return I
def multip(M1,M2,n):
    M3=[]
    for l1 in range (n):
        M3.append([0]*(n))

    for x in range (n):
        for y in range (n):
            suma=0
            for z in range (n):
                suma=suma+M1[x][z]*M2[z][y]
            M3[x][y]=suma
    return M3
def parletreid(aa,bb,nn):
    global A,a,b,n
    a = aa[:]
    b = bb[:]
    n = nn
    init()
    I=[]
    P=[]
    M=[]
    L=[]
    U=[]
    T=[]
    G=[]
    F=[]
    S=[]
    PP=[]
    W=[]
    PPT=[]
    b=[]
    for i in range (n):
        I.append([0]*(n))
        PPT.append([0]*(n))
        P.append([0]*(n))
        W.append([0]*(n))
        M.append([0]*(n))
        L.append([0]*(n))
        PP.append([0]*(n))
        U.append([0]*(n+1))
        T.append([0]*(n+1))
        S.append([0]*(n+1))
        G.append(0)
        F.append(0)
        b.append(0)
        P[i][i]=1
        PP[i][i]=1
        I[i][i]=1
        W[i][i]=1


    for i in range(n):
        L[i][i]=1
    for i in range(n):
        for j in range(n+1):
            T[i][j]=A[i][j]
   
   #algoritmo#
    for i in range(n-2):
        P=[]
        for j in range (n):
            P.append([0]*(n))
            P[j][j]=1
        for j in range(n):
            for k in range(n):
                S[j][k] = I[j][k]
        #Pivoteo#
        p = i+1       
        mayor = abs(T[i+1][i])
        for j in range (i+2,n):    
            if mayor < abs(T[j][i]):
                mayor = abs(T[j][i])
                p = j
        P[i+1] = S[p]
        P[p] = S[i+1]       
    #multiplicacion PAPT#
        F=T[i+1]
        T[i+1] = T[p]
        T[p] = F        
        for j in range(n):
            for k in range(n+1):
                U[j][k] = T[j][k]       
        for j in range (n):
            for k in range (n):
                suma = 0
                for l in range (n):
                    suma = suma + U[j][l]*P[k][l]
                T[j][k] = suma
    #Gauss#
        for j in range (n):
            G[j]=0
            U.append([0]*(n+1))
        for j in range (i+2,n):
            G[j] = U[j][i]*(U[i+1][i]**(-1))        
    #matriz de gaus#
        for j in range (n):
            for l in range (n):
                M[j][l] = S[j][l] - G[j]*I[i+1][l]       
    #multiplicacion MPAPTMT#                
        for j in range(n):
            for k in range(n+1):
                U[j][k] = T[j][k]        
        for j in range(n):
            for k in range(n):
                suma = 0
                for l in range(n):
                    suma = suma  + M[j][l]*U[l][k]
                T[j][k] = suma
        for j in range(n):
            for k in range(n+1):
                U[j][k] = T[j][k]        
        for j in range(n):
            for k in range(n):
                suma = 0
                for l in range(n):
                    suma = suma  + U[j][l]*M[k][l]
                T[j][k] = suma
        
    #EL P TOTAL#
        for j in range(n):
            for k in range(n):
                suma = 0
                for l in range(n):
                    suma = suma + P[j][l]*W[l][k]
                PP[j][k] = suma
        for j in range (n):
            for k in range(n):
                W[j][k]=PP[j][k]
    #M2P2M1P1#
        L= multip(multip(M,P,n),L,n)            
    for j in range(n):
        for k in range(n):
            PPT[j][k]=PP[k][j]
    L=multip(L,PPT,n)
    L=inversa(L,n)
    Q=[]
    for s in range (n+1):
        Q.append(0)
    Lt=[]
    for s in range (n):
        Lt.append([0]*n)    
    z=[]
    for i in range (n):
        z.append(0)
    z[0]=T[0][n]*(L[0][0]**(-1))
    for j in range (1,n):       
        suma=0
        for k in range (j):
            suma+= L[j][k]*z[k]
        z[j]=(T[j][n]-suma)*(L[j][j]**(-1))
    
    for i in range (n):
        j=i+1
        if T[i][i]==0:
            p=i+1
            mayor = T[j][i]
            for j in range (i+2,n):
                if(abs(mayor) < abs(T[j][i])):
                    mayor= T[j][i]
                    p = j
            
            Q=T[i]
            T[i]=T[p]
            T[p]=Q
            k=z[i]
            z[i]=z[p]
            z[p]=k
        for j in range (i+1,n):
            w = T[j][i]*(T[i][i])**(-1)
            for k in range (i,n+1):
                T[j][k] = T[j][k] - (w*T[i][k])
                T[j][i]=0
            z[j] = z[j] - (w*z[i])


    W=[]
    for i in range (n):
        W.append(0)
    W[n-1]=z[n-1]/T[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= T[j][k]*W[k]
        W[j]=(z[j]-suma)/T[j][j]

    for i in range(n):
        for j in range (n):
            Lt[i][j]= L[j][i]
    y=[]
    for i in range (n):
        y.append(0)
    y[n-1]=W[n-1]/Lt[n-1][n-1]
    for j in range (n-2,-1,-1):
        suma=0
        for k in range (j+1,n):
            suma+= Lt[j][k]*y[k]
        y[j]=(W[j]-suma)*(Lt[j][j]**(-1))

    x=[]
    for i in range (n):
        x.append(0)
    for j in range(n):
        suma = 0
        for l in range(n):
            suma=suma+PPT[j][l]*y[l]
        x[j]=suma
    
    ans = ''
    ans += 'Parlet-Reid'
    ans += '\n' + str(x) + '\n\n'
    return ans
