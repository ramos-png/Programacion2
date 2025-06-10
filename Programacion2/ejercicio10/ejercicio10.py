# Ejercicio 10. diseñar una funcion que devuelva el factorial de un numero
# entero ingresado
 

def calcular_facto(num):
    fact=num
    for i in range(1,num,1):
        fact=fact*i
    return fact

num=0
print('Ingrese el numero que quiera factorizar.')
num=int(input())

fact=calcular_facto(num)

print('El factorial es: ' , fact)
