"""
Problem 3: Average of numbers with while and sentinel

Descripción:
Lee números uno por uno hasta que el usuario ingrese un valor 
sentinela (por ejemplo, -1). Calcula el promedio de los números válidos 
ingresados y la cantidad de números leídos. Si el usuario sólo ingresa 
el sentinela sin números válidos, muestra un mensaje de error.

Entradas:
- number (float; se lee repetidamente).
- sentinel_value (fijo en el código, por ejemplo: -1).

Salidas:
- "Count:" <count>
- "Average:" <average_value>
- Si no se ingresan datos válidos:
  - "Error: no data"

Validaciones:
- Cada lectura debe intentar convertirse a float.
- Ignorar el sentinela en los cálculos.

"""
count = 0
total_sum = 0

while True:
    try:
        number = float(input("Enter the number: "))
        if number == -1:
            break 

    except: 
        print("Error Invalid Input")
        continue
    
    count += 1
    total_sum += number
    avg_value = total_sum/count
if count == 0:
    print("Error No Data")
else:
    print(f"Count: {count}")
    print(f"Average: {avg_value}")

"""
# Test Case 1:
# Input:
# 5
# 10
# -1
# Output:
# Count: 2
# Average: 7.5

# Test Case 2:
# Input:
# -1
# Output:
# Error No Data

# Test Case 3:
# Input:
# a
# 3
# 3
# -1
# Output:
# Error Invalid Input
# Count: 2
# Average: 3.0
"""