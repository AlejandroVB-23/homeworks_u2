"""
Nombre: Anuar Alejandro Vazquez Balderas
Grupo: 1-1 IM
Matricula: 2530390

Resumen Ejecutivo: 
La serie de Fibonacci es una sucesión numérica donde cada término se obtiene 
sumando los dos anteriores, comenzando normalmente con 0 y 1. Calcular 
la serie hasta un número de términos n significa generar los primeros n 
valores siguiendo esa regla.
El programa leerá el valor de n ingresado por el usuario, realizará una 
validación básica para asegurar que sea un entero positivo y, finalmente, 
producirá y mostrará la serie completa de Fibonacci hasta alcanzar la cantidad 
de términos solicitados.


Problem: Fibonacci series generator  
Description: Program that reads an integer n and prints the first n terms of the Fibonacci series starting at 0 and 1.  

Inputs:  
- n (int; number of terms to generate)  

Outputs:  
- "Fibonacci series:" followed by the n terms separated by spaces or commas  

Validations:  
- n must be an integer  
- n must be >= 1  
- (Optional) n must be <= 50  
"""

print("Fibonacci Series")
try: 
    n = int(input("Enter the term of the series. >0 and <50: "))
    if n > 0 and n < 50:
        p1 = 0
        p2 = 1
        fib_list = []
        for i in range(n):
            fib_list.append(p1)
            acumulator = p1
            p1 = p2
            p2 = acumulator+p2
        print(f"Number of terms: {n}")
        print(f"Fibonacci Series: {fib_list}")
    else:
        print("Error: Invalid Input")
except:
    print("Error Invalid Input")

"""
Test Cases:
# Test Case 1 (Normal):
# Input:
# n = 6
# Fibonacci -> [0, 1, 1, 2, 3, 5]
# Expected Output:
# Number of terms: 6
# Fibonacci Series: [0, 1, 1, 2, 3, 5]


# Test Case 2 (Borde):
# Input:
# n = 1
# Fibonacci -> [0]
# Expected Output:
# Number of terms: 1
# Fibonacci Series: [0]


# Test Case 3 (Error):
# Input:
# n = -4
# Expected Output:
# Error: Invalid Input

Conclusiones: 
El uso de un bucle permitió generar la serie de Fibonacci de manera ordenada 
y repetitiva, evitando cálculos manuales y asegurando que cada término se 
construyera correctamente. Manejar los casos especiales n = 1 y n = 2 
es importante porque representan los inicios de la serie,  y un error allí 
afectaría todos los cálculos posteriores. Esta misma lógica puede reutilizarse 
en programas que requieran patrones repetitivos, procesos acumulativos 
o simulaciones basadas en pasos secuenciales.


Referencias:
1) https://www.datacamp.com/es/tutorial/fibonacci-sequence-python
2) https://ellibrodepython.com/for-python
3) https://realpython.com/fibonacci-sequence-python/


GitHub Repo Link: 
https://github.com/AlejandroVB-23/homeworks_u2.git
"""