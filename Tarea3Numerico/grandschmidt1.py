import math
m = int(raw_input("Ingrese m: "))
n = int(raw_input("Ingrese n: "))
 
a = []          # m*n
A = []                  # m*n
b = []                  # m*1
U = []                  # n*n
E = []                  # m*n
Et = []                 # n*m
x = []                  # n*1
 
for i in range (m):
        A.append([])
        a.append([])
        E.append([])
        for j in range (n):
                A[i].append(float(raw_input()))
                a[i].append(float(A[i][j]))
                E[i].append(0.0)
#               if i == j:
#                       E[i].append(1.0)
#               else:
#                       E[i].append(0.0)
 
print 'matriz E:'
for i in range(m):
        print E[i]
print'\n'
 
 
for i in range(m):
        b.append(float(raw_input()))
       
for i in range(n):
        U.append([])
        for j in range(n):
                U[i].append(0.0)
 
for i in range(n):
        Et.append([])
        x.append(0.0)
        for j in range(m):
                Et[i].append(0.0)
 
 
for j in range(n):
        for i in range(j):
                prod_int = 0.0          #producto interno de ET[][].A[][]
                for k in range(m):
                        prod_int += Et[i][k]*a[k][j]   
                U[i][j] = prod_int
               
                for k in range (m):
                        E[k][j] = a[k][j] - U[i][j]*E[k][i]
                        Et[j][k] = E[k][j]             
               
                suma=0.0
                for k in range(m):
                        suma += E[k][j]*E[k][j]
                U[j][j] = math.sqrt(suma)
               
                for k in range(m):
                        E[k][j] = E[k][j]/U[j][j]
                        Et[j][k] = E[k][j]
                       
#for i in range(m):
#       for j in range(n):
#               Et[j][i] = E[i][j]
 
B = []
 
for i in range(n):
        B.append(0.0)
 
for i in range(n):
        for j in range(m):
                B[i] = B[i]+ Et[i][j]*b[j]
       
 
print 'matriz A:'
for i in range(m):
        print a[i]
print'\n'
 
print 'matriz b:'
for i in range(m):
        print b[i]
print'\n'
 
print 'matriz U:'
for i in range(n):
        print U[i]
print'\n'
 
print 'matriz E:'
for i in range(m):
        print E[i]
print'\n'
 
print 'matriz Et:'
for i in range(n):
        print Et[i]
print'\n'
 
print 'matriz B:'
for i in range(n):
        print B[i]
print'\n'      
 
print B[2],U[2][2],B[2]/U[2][2]
 
j = n-1
while j>=0:
        res = B[j]
        for k in range (j+1, n):
                res -= U[j][k] *x[k]
        res /= float(U[j][j])
        x[j] = res
        print j, res
        j-=1
 
print 'matriz x:'
for i in range(n):
        print x[i]
print'\n'
