# Ejercicio 6. Un cajero automatico entrega solo billetes de $1000 y de $200
# Ingresar la cantidad que desea extraer el usuario y luego indicar cuàntos
# billetes de $1000 y $200 se le entregan al cliente. Indicar ademàs el saldo
# que no se pudo extraer porque no hay billetes

PlataBanco=10000
plata=0
resto=0
cont1=0
cont2=0


print('Ingrese la cantidad de dinero que quiere retirar')
print('Ingrese una cifra multiplo de 200 ')
plata=int(input())


resto=(plata%1000)

if(plata//1000):
    cont1=cont1+1
else:
    if(resto//200):
        cont2=cont2+1

print('dos' , cont2)
print('mil' , cont1)

    
