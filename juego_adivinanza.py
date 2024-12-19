import random

numero_secreto = random.randint(1,101)
cant_intentos = 0
cant_mx_intentos = 5
adivinado = False

print ('Bienvenidx al juego de adivinar el numero secreto')

while not adivinado:
    if not cant_intentos < cant_mx_intentos:
        print("GAME OVER!!")
        break
   
    numero = int(input('Introduce un numero del 1 al 100:'))

    if numero == numero_secreto:
        print ('Adivinaste!!')
        adivinado = True
    elif numero < numero_secreto:
        print ('El numero es mayor al ingresao')
    else:
        print('El numero es menor al ingresado')
    cant_intentos +=1