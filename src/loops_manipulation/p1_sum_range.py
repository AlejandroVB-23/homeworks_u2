"""
Problem 1. Sum of range

Descripción:
Calcula la suma de todos los enteros desde 1 hasta n (incluyendo n). Además, calcula la suma solo de los números pares en ese mismo rango usando un bucle for.

Entradas:
- n (int; límite superior del rango).

Salidas:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>

Validaciones:
- Verificar que n pueda convertirse a int.
- n >= 1; si no se cumple, mostrar "Error: invalid input".
"""
print("Sum of range")
total_sum=0
even_sum=0
try:
    n = int(input("Enter the terms to sum: "))
    if n >= 1:
        for i in range(1,n+1):
            total_sum += i
        
        for i in range(0,n+1,2):
            even_sum += i
        print(f"Sum 1 up to {n}: {total_sum}")
        print(f"Even sum 1 up to {n}: {even_sum}")
    else:
        print("Error Invalid Input")
except:
    print("Enter a valid input")
"""
# Test Case 1 (Normal):
# Input:
# n = 5
# total_sum -> 1 + 2 + 3 + 4 + 5 = 15
# even_sum  -> 0 + 2 + 4 = 6
# Expected Output:
# Sum 1 up to 5: 15
# Even sum 1 up to 5: 6


# Test Case 2 (Borde):
# Input:
# n = 1
# total_sum -> 1
# even_sum  -> 0
# Expected Output:
# Sum 1 up to 1: 1
# Even sum 1 up to 1: 0


# Test Case 3 (Error):
# Input:
# n = 0
# Expected Output:
# Error Invalid Input
"""