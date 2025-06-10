# Ejercicio N°3. Conversor Decimal-Binario-Hexadecimal
# Diseñar un programa que muestre el número ingresado por el usuario en sistema
# decimal, binario y hexadecimal

opcion=0
num=0
hexa=0
bina=0

print('Convertir a Hexadecimal (1)')
print('Convertir a Binario (2)')
opcion=int(input())

print('Ingrese su número decimal')
num=int(input())


if(opcion==1):
    num=hex(num)
    print('Su número en hexadecimal es : ' , num)

else:
    num=bin(num)
    print('Su número en binario es : ' , num)
    
    
    
    