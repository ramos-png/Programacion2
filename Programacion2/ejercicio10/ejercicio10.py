# Ejercicio 10. diseñar una funcion que devuelva el factorial de un numero
# entero ingresado
 

num=0
fact=1

print('Ingrese un numero entero')
num=int(input())

for i in range (1,num+1,1):
    fact=fact*i

print('El factorial del numero ingresado es ' , fact)
