#Ejercicio 2

n= 
Ma1=matrix(0,n,n) #Aqui se crea la matriz de ceros
Ma2=matrix(rep(0,n*(n-1)),n)

#Creamos una matriz de propuestas para c/p
for(i in 1:n)
{
  Ma2(i,)=sample(c(1:n)[-i],n-1)
}
cont=0  #Aqui contamos el numero de parejas.

parejas=rep(0,n) #Le Asignamos el "0".

#Leemos la matriz en n-1
for(j in 1:(n-1))
{
  Ma1=matrix(0,n,n) #Se creo de nuevo la matriz de ceros y hacemos la matriz de Ma1 con el tamaño de la matriz original.
}

#Asignamos 1 a las personas con propuestas
for(i in 1:n)
{
  Ma1(i,Ma2(i,j))=1
}

#Creamos una matriz simetrica

for(i in 1:n)

{
  for(j in 1:(n-1))
  {
    Ma1(i,j)=Ma1(j,i)
  }
  
}

Ma2
Ma1


#Aqui Contamos el numero de propuestas que se tiene por persona

for(i in 1:n)
{
  if(sum(Ma1(,i)) >= 1)   #Sumamos el numero de propuestas de las personas
  {
   propuesta=wich(Ma1==1)
   cont=cont + 1
   parejas(i)=1
  }
}


propuesta_Solu=NULL   #Nota: detenemos el codigo si ya se formaron todas las parejas posibles

# Aqui checamos que chicos estan solteritos para asignarles su parejita
for(k in propuesta)
{
  if(parejas(k)==0)  #Si alguno de los chicos solterukis consigue parejilla, sale de la jugada y nos pasamos con los otros nenorros
  {
    propuesta_Solu=c(propuesta_Solu,k)
  }
}

propuesta=propuesta_Solu  #Entonces las propuesta ahora  serian igual a la propuesta solucion por que ya le asignamos una parejilla a un chico que andaba solteruki 

#Aqui checamos las lista de preferencias de las personas
for(j in 1:(n-1))
{
  if(sum(Ma2(i,j)==propuesta)==1)
}
  pareja=propuesta(wich(Ma2(i,j)==propuesta))

#Aqui el chico o chica Rechaza los pretendientes que no estan en sus preferencias

  Ma1(-pareja,i)=0  #Aqui de la matriz 1, le quitamos una de las parejas, para que vallan quedando solo las personas sin parejilla
  cont=cont +1    #Aqui sumamos a las parejas 

#Aqui actualizamos si las personas estan solterillos o con parejilla
  parejas(i)=1       #Si los que andaban solterukis ya tienen pareja y se forma una pareja se asignara el 1
  parejas(pareja)=1  #Entonces aqui las parejas de pareja de dos se ponen en 1


#Aqui se Contempla el dato donde se tenga un solo pretendiente
  else if(sum(Ma1(,i))==1)
  {
    pretendiente=which(Ma1(,i)==1)
  
  if(sum(M(,pretendiente))==1)  #Revisamos que ese pretendiente este soltero por que aqui no existen las infidelidades
   {
     pareja=pretendiente   #Aqui se ve si ese pretendiente ya tiene una pareja asignada
     Ma1(-pareja,i)=0   #Aqui a la matriz 1 le quitamos una pareja y le ponemos el 0
    
      if(cont==n/2)   #Se detiene el codigo si ya se formaron las parejas posibles
       {
        j=n
        i=n+1
       }
  
   } 
}

Ma2    
Ma1
 





