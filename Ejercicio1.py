# 1. Escriba un programa que reciba como entrada un número entero n, y entregue como salida el n-
# ésimo número de Fibonacci:


try:

    Numero = int(input("\nIngresa N: \t"))

    Fibonacci = [0,1]

    for i in range(1,Numero):
        Fibonacci.append(Fibonacci[-1] + Fibonacci[-2])
    
    if Numero == 0:
        print(f"\nEn la posicion {Numero} es: {Fibonacci[0]}") 
    elif Numero < 0:
        print("\nNo se aceptan numeros negativos")
    else:
        print(f"\nEn la posicion {Numero} es: {Fibonacci[-1]}")

except:
    print("\nIngresa un numero Valido")