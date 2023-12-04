# 3. Escriba un programa que muestres los m primeros números de Fibonacci, donde m es un número
# ingresado por el usuario:

try:

    Numero = int(input("\nIngresa M: \t"))

    Fibonacci = [0,1]

    for i in range(1,Numero - 1):
        Fibonacci.append(Fibonacci[-1] + Fibonacci[-2])
    
    if Numero < 0:
        print("\nNo se aceptan numeros negativos")
    elif Numero == 1:
        print(f"\nLos {Numero} primeros numero de Fibonacci Son:") 
        print("[0]")
    elif Numero == 0:
        print(f"\nLos {Numero} primeros numero de Fibonacci Son:") 
    else:
        print(f"\nLos {Numero} primeros numero de Fibonacci Son:") 
        print(Fibonacci)

except:
    print("\nIngresa un numero Valido")