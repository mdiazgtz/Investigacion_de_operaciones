'''
Resolver el problema del agente viajero utilizando un algoritmo.
*Empieza desde el punto k y toma el camino más corto
*No pasa por el mismo camino 2 veces

Para yo resolver esto, cuando un camino no tiene acceso directo a un lugar coloqué un 50
'''

op='k'
while op!='a' and op!='b' and op!='c' and op!='d' and op!='e' and op!='f':
    print('\n\n\t Elige la ciudad a comenzar: ')
    print('\t a) Cd a \n\t b) Cd b  \n\t c) Cd c  \n\t d) Cd d  \n\t e) Cd e  \n\t f) Cd f')
    op= input('\t\t\t-->')
    if  op!='a' and op!='b' and op!='c' and op!='d' and op!='e' and op!='f':
        print('\tERROR AL CAPTURAR OPCIÓN\n')

if op=='a':
    ciudad=1
elif op=='b':
    ciudad=2
elif op=='c':
    ciudad=3
elif op=='d':
    ciudad=4
elif op=='e':
    ciudad=5
elif op=='f':
    ciudad=6



cd=[1,2,3,4,5,6]
dis=[[0,7,5,6,4,50], [7,0,8,50,6,4], [5,8,0,8,50,7], [6,50,8,0,7,6], [4,6,50,7,0,6], [50,4,7,6,6,0]]
dis2=[[0,7,5,6,4,50], [7,0,8,50,6,4], [5,8,0,8,50,7], [6,50,8,0,7,6], [4,6,50,7,0,6], [50,4,7,6,6,0]]

n=len(cd)
a= []
for w in range (0,n):
    p=len(dis[w])
    g=p #Se utilizará para valores repetidos
    for i in range (0,p):
        #mínimo de la lista
        if g==0: 
            break
        orden= min(dis2[w])

        for j in range (0,p):
            #Encuentra la posición del mínimo de la lista original y lo agrega a la lista a
            if (orden==dis[w][j]):
                b=j
                a.append(b)
                g-=1
                
                for z in range (0,p-i):
                    if (orden==dis2[w][z]):
                        del(dis2[w][z])
                        break

c= []
for i in range (0,n):
    b= []
    for j in range (0,n):
        o= a[j+(i*6)]
        b.append(o)
    c.append(b)
    del(b)

camino= []
aqui=ciudad-1
camino.append(aqui)

for i in range (0,n-1):
    k= 0
    for i in range (0,n-1):
        orden= c[aqui][k]
        if orden in camino:
            k+=1
        else:
            aqui=orden
            break
    camino.append(aqui)


print('\n\n\t PASOS')
for i in range (0,n):
    print('\tPaso: ', i+1, ' camino: ', camino[i]+1)

suma=0
for i in range (0,n-1):
    t=camino[i]
    tt=camino[i+1]
    suma+= dis[t][tt]

print('\n\t Distancia recorrida: ', suma)