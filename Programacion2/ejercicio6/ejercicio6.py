# Ejercicio 6. Un cajero automatico entrega solo billetes de $1000 y de $200
# Ingresar la cantidad que desea extraer el usuario y luego indicar cuàntos
# billetes de $1000 y $200 se le entregan al cliente. Indicar ademàs el saldo
# que no se pudo extraer porque no hay billetes

PlataBanco=10000
usuario=0
resto=0
dos=0
mil=0
deuda=0


print('Ingrese la cantidad de dinero que quiere retirar')
print('Su presupuesto es de 10000$')
usuario=int(input())

if(usuario<=10000)and(usuario>1):
    mil=(usuario//1000)
    resto=(usuario-(mil*1000))
    dos=(resto//200)
    print('Billetes de mil: ' , mil)
    print('Billetes de doscientos: ' , dos)
else:
    if(usuario>10000):
        print('No puede retirar esa cantidad exacta.')
        deuda=(usuario-PlataBanco)
        print('No tiene dinero suficiente para retirar. faltan:',deuda,'$')
        
