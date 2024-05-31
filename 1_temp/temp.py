temperatura = float(input("ingrese la temperatura de ahora: "))
tipoDeEscala =  input("(F) si es Farahemnt o (C)si es Celcious: ").lower()

if tipoDeEscala == "c":
    temp_C = (temperatura * 9/5) + 32
    print(f'esta haciendo {temp_C} c')
elif tipoDeEscala == "f":
    temp_F = (temperatura - 32) * 5/9
    print(temp_F)
else:
    print("escala invalida.")

