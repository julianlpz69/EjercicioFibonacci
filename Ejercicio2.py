# 2. Escriba un programa que reciba como entrada un número entero e indique si es o no un número
# de Fibonacci:



try:

    Numero = int(input("\nIngresa N: \t"))
    
    if Numero == 0:
        print(f"\n{Numero} Si es un numero Fibonacci en la posicion 0")
    elif Numero == 1:
        print(f"\n{Numero} Si es un numero Fibonacci en la posicion 1")
    elif Numero < 0:
        print(f"\nLos negativos no son numeros Fibonacci")
    
    else:
        Fibonacci = [0,1]

        while Numero >= Fibonacci[-1]:
            Fibonacci.append(Fibonacci[-1] + Fibonacci[-2])
            
            if Fibonacci[-1] == Numero:
                print(f"\n{Numero} Si es un numero Fibonacci en la posicion {len(Fibonacci)-1}")
                break
            elif Fibonacci[-1] > Numero:
                print(f"\n{Numero} No es un numero Fibonacci")
                
except:
    print("\nIngresa un numero Valido")