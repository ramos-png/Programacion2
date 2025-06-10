# Ejercicio 5. Un profe tiene X caramelos para repartir entre Y estudiantes.
# Los estudiantes deben recibir un mùmero entero de caramelos. Preguntar al 
# usuario cuàntos estudiantes y luego indicar cuàntos le tocan a cada estudiante
# y cuantos sobran en la bolsa,


caramelos=200
estudiantes=0
division=0
resto=0

print('Cuantos estudiantes hay?')
estudiantes=int(input())

division=(caramelos // estudiantes)
rest=(caramelos % estudiantes)

print('El profesor tendrà que repartir ' , division , ' caramelos entre ' , estudiantes , ' alumnos ')
print('Y sobran ' , rest , ' de caramelos en la bolsa.')
