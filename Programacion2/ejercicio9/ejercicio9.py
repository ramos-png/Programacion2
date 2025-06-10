# Ejercicio 9. Escribir una funcion que calcule el total de una factura tras aplicarle el IVA. La funcion debe recibir el importe 
# sin IVA y el porcentaje de IVA a aplicar. Si se invoca la funcion sin pasarle el porcentaje del IVA , debera aplicar el 21%

iva1=15
iva2=21
precio=0
opc=0
porcentaje=0
total=0

print('Ingrese el precio del objeto a pagar')
precio=int(input())

print('¿Que porcentaje de IVA quiere utilizar?')
print('(1) 15%')
print('(2) 21%')
opc=int(input())

if(opc == 1):
    print('Eligio el porcentaje del 15%')
    porcentaje=iva1/100+1
    total=precio*porcentaje
    print('El precio total es de ' , total)
else:
    if(opc == 2):
        print('Eligio l porcentaje del 21%')
        porentaje=iva2/10+1
        total=precio*porentaje
        print('El precio total es de ' , total)
    else:
        print('puto el que lo lea')
    
    
    
    
    
    
    
    