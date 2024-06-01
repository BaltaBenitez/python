num1 = int(input('Númro 1: '))
num2 = int(input('Númro 2: '))
op = input('Introduce una operacion: (+ - x /): ')

match op:
    case '+':
        respuesta = num1 + num2
    case '-':
        respuesta = num1 - num2
    case 'x':
        respuesta = num1 * num2
    case '/':
        respuesta = num1 / num2
        
print(f'EL RESULTADO DE {num1} Y {num2} ES {respuesta}')