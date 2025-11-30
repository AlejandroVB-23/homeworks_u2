"""
Problem 4. Basic statistics of three integers
Descripción:
Lee tres números enteros y calcula: suma, promedio (float), 
valor máximo, valor mínimo y un booleano all_even que indique
 si los tres números son pares.

Entradas:
- n1 (int)
- n2 (int)
- n3 (int)

Salidas:
- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false

Validaciones:
- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).
"""
print("Basic statistics of three integers")
try: 
    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    n3 = int(input("Number 3: "))
    sum_value = n1+n2+n3
    average_value = sum_value/3
    max_value = max(n1,n2,n3)
    min_value = min(n1,n2,n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    print(f"Sum: {sum_value}") 
    print(f"Average: {average_value}") 
    print(f"Max: {max_value}") 
    print(f"Min: {min_value}")
    print(f"All Even: {all_even}")
except: 
    print("All numbers must be integers")