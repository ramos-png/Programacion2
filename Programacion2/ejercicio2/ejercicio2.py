import random

num1=0
use=0
cont=0

num1=random.randint(1,20)

while(cont<6 or use==num1):
    print('Ingrese un número del 1 al 20')
    use=int(input())
    if(use>0 and use<21):
        if(use==num1):   
            print('ganaste')
        else:
            if(use<num1):    
                print('tu numero es menor')   
            else:
                (use>num1)
                print('tu numero es mayor')
    else:
        print('tu numero es invalido')
        cont=cont+6
cont=cont+1

  
        
        
    