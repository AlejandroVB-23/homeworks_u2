"""
Problem 3. List Numbers
Descripción:
Define una función summarize_numbers(numbers_list) que reciba una 
lista de números y regrese un diccionario con:
- "min": mínimo
- "max": máximo
- "average": promedio (float)
El código principal debe construir la lista (por ejemplo, a partir d
e texto separado por comas), llamar la función y mostrar los valores.

Entradas:
- numbers_text (string; por ejemplo, "10,20,30")
- Internamente: numbers_list (list of float o int)

Salidas:
- "Min:" <min_value>
- "Max:" <max_value>
- "Average:" <average_value>

Validaciones:
- numbers_text no vacío tras strip().
- Lista no vacía después de la conversión.
- Todos los elementos deben poder convertirse a números; si alguno falla, 
mostrar "Error: invalid input".
"""


def summarize_numbers(numbers_list):
    
    result = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return result


numbers_text = input("Ingresa números separados por comas: ")


if not numbers_text.strip():
    print("Error: invalid input")
else:
    try:
        
        numbers_list = [float(num.strip()) for num in numbers_text.split(",") if num.strip()]

        
        if not numbers_list:
            print("Error: invalid input")
        else:
            
            summary = summarize_numbers(numbers_list)

            print("Min:", summary["min"])
            print("Max:", summary["max"])
            print("Average:", summary["average"])

    except: 
       
        print("Error: invalid input")

"""
# Test Case 1  
# Entrada válida con números positivos y negativos
Input:    "10, 20, -5, 15"
Output:
Min: -5
Max: 20
Average: 10.0

# Test Case 2  
# Entrada con espacios, valores flotantes y formato irregular
Input:    "  3.5 , 7 ,  10.5 ,2 "
Output:
Min: 2.0
Max: 10.5
Average: 5.75

# Test Case 3  
# Entrada inválida: contiene texto no numérico
Input:    "4, 8, hola, 10"
Output:
Error: invalid input

"""