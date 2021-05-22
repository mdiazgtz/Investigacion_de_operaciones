'''
Diseñe y ejecute computacionalmente un algoritmo para resolver el problema de múltiples 
mochilas.
'''

#OBTENIENDO DATOS
m=0
while m<=0:
    m= int(input("\n Introduce el número de mochilas: "))
    if m<=0:
         print('\tERROR AL CAPTURAR NÚMERO DE MOCHLAS\n')


print('\n')
capm= []
for i in range (0,m):
    cap=0
    while cap<=0:
        cap= float(input("Introduce la capacidad (en kg) de la mochila %d: " %(i+1)))
        if cap<=0:
            print('\tERROR AL CAPTURAR CAPACIDAD DE MLA MOCHILA\n')
    capm.append(cap)


print('\n')
p=0
while p<=0:
    p= int(input("Introduce el número total de productos: "))
    if p<=0:
         print('\tERROR AL CAPTURAR NÚMERO DE PRODUCTOS\n')


print('\n')
pesop= []
pesop2= []
for i in range (0,p):
    peso=0
    while peso<=0:
        peso= float(input("Introduce el peso del producto %d: " %(i+1)))
        if peso<=0:
            print('\tERROR AL CAPTURAR EL PESO DEL PRODUCTO\n')
    pesop.append(peso)
    pesop2.append(peso)



#ordenando por peso
print('\n\t ORDENANDO POR PESO\n')
a= []
g=p #Se utilizará para valores repetidos
for i in range (0,p):
    #mínimo de la lista
    if g==0: 
        break
    orden= min(pesop2)

    for j in range (0,p):
        #Encuentra la posición del mínimo de la lista original y lo agrega a la lista a
        if (orden==pesop[j]):
            b=j
            a.append(b)
            g-=1
            
            for z in range (0,p-i):
                if (orden==pesop2[z]):
                    del(pesop2[z])
                    break

#Procedimiento
capmi= []
for z in range (0,m):
    c=capm[z]
    capmi.append(c)

j=0
for i in range (0,m):
    print('\nProductos de la mochila #', i+1)
    for z in range(j,p):
        k=a[j]
        capmi[i]-=pesop[k]
        if capmi[i]<0:
            capmi[i]+=pesop[k]
            break
        if capmi[i]==0:
            print('\t Producto #', k+1)
            j+=1
            break
        print('\t Producto #', k+1)
        j+=1