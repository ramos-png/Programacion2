# Ejercicio N°4. Una bacteria se reproduce en un lapso de 1 hora. Luego, por cada 
# hora que pasa cada bacteria se reproduce en otra. Preguntar al usuario cuántas
# horas pasaron e indicar cuántas bacterias habrá.

bac=0
hora=1

print('¿Cuántas horas pasaron?')
hora=int(input())

for i in range(0,hora,1):
    bac=2**hora
print('horas:' , hora)
print('bacterias:' , bac)