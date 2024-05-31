import random

n = random.randint(1, 6)
msg = int(input('Elige un número del 1 al 6: '))

if msg < 1 or msg > 6:
    print('Valor incorrecto. Elija un número entre 1 y 6.')
elif msg == 1: 
    print('PERDISTE. Borrando System32..')
else:
    print('GANASTE :D')