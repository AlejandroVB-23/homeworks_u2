"""
Nombre: Anuar Alejandro Vazquez Balderas
Matricula: 2530390
Grupo: 1-1 IM

Resumen Ejecutivo: 
Una función en Python es un bloque de código diseñado para ejecutar
una tarea específica sin repetir instrucciones innecesariamente.
Los parámetros se escriben en la definición de la función y los
argumentos se envían cuando la función es llamada en el programa.
Dividir el programa en funciones mejora la claridad y la posible
reutilización del código en diferentes partes del proyecto.
El valor de retorno es el dato que la función entrega y permite
usar ese resultado en cálculos posteriores, no solo imprimirlo.
El documento cubrirá descripción, funciones, entradas, salidas,
validaciones y pruebas de funcionamiento básicas.
"""
"""
Problem 1: Rectangle area and perimeter
Descripción:
Define dos funciones:
- calculate_area(width, height): regresa el área de un rectángulo.
- calculate_perimeter(width, height): regresa el perímetro.
El código principal debe leer (o definir) los valores, llamar a las 
funciones y mostrar los resultados.

Entradas:
- width (float)
- height (float)

Salidas:
- "Area:" <area_value>
- "Perimeter:" <perimeter_value>

Validaciones:
- width > 0
- height > 0
- Si alguna condición no se cumple, mostrar "Error: invalid input" y 
no llamar a las funciones.
"""

def calculate_area(w, h):
  area_value = w*h
  return area_value
def calculate_perimeter(w,h):
  perimeter_value = 2*(w+h)
  return perimeter_value

try: 
  width = float(input("Enter the width: "))
  height = float(input("Enter the height: "))

  if not width == 0 or not height == 0:
    print(f"Area: {calculate_area(width,height)}")
    print(f"Perimeter: {calculate_perimeter(width,height)}")
  else:
    print("Error Invalid Input")
except:
  print("Error Invalid Input")

"""
Test Cases

1) Caso Normal
Entrada:
    Enter the width: 5
    Enter the height: 3
Salida esperada:
    Area: 15.0
    Perimeter: 16.0

2) Caso Borde (uno de los valores = 0, debería marcar error
pero el código actual NO lo detecta por el uso incorrecto del if)
Entrada:
    Enter the width: 0
    Enter the height: 4
Salida esperada lógica esperada:
    Error Invalid Input
Salida real del programa:
    Area: 0.0
    Perimeter: 8.0

3) Caso Error (entrada no numérica)
Entrada:
    Enter the width: hola
    Enter the height: 5
Salida esperada:
    Error Invalid Input
"""
"""
Problem 2. Grade Classifier
Descripción:
Define una función classify_grade(score) que reciba una calificación numérica (0–100) y regrese una categoría:
- "A" si score >= 90
- "B" si 80 <= score < 90
- "C" si 70 <= score < 80
- "D" si 60 <= score < 70
- "F" si score < 60
El código principal debe llamar la función y mostrar el resultado.

Entradas:
- score (float o int)

Salidas:
- "Score:" <score>
- "Category:" <grade_letter>

Validaciones:
- 0 <= score <= 100
- Si no se cumple, mostrar "Error: invalid input" y no clasificar.
"""
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
try:
    score_text = input("Enter score (0–100): ").strip()

    if score_text == "":
        print("Error: invalid input")
        exit()
    score = float(score_text)
    if not (0 <= score <= 100):
        print("Error: invalid input")
        exit()
    grade = classify_grade(score)
    print(f"Score: {score}")
    print(f"Category: {grade}")
except:
    print("Error: invalid input")

"""
Test Cases

1) Caso Normal
Entrada:
    Enter score (0–100): 85
Salida esperada:
    Score: 85.0
    Category: B

2) Caso Borde (límite superior de cambio de categoría)
Entrada:
    Enter score (0–100): 90
Salida esperada:
    Score: 90.0
    Category: A

3) Caso Error (fuera de rango)
Entrada:
    Enter score (0–100): 120
Salida esperada:
    Error: invalid input
"""
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
"""
Problem 4. Apply Discount List
Descripción:
Define una función apply_discount(prices_list, discount_rate) que:
- reciba una lista de precios (float) y una tasa de descuento (por ejemplo, 0.10 para 10%)
- regrese una nueva lista con los precios ya descontados (no modificar la lista original).
El código principal debe:
- Crear una lista de precios.
- Llamar a la función.
- Mostrar la lista original y la nueva lista con descuento.

Entradas:
- prices_text (string; por ejemplo, "100,200,300")
- discount_rate (float, entre 0 y 1)

Salidas:
- "Original prices:" <original_list>
- "Discounted prices:" <discounted_list>

Validaciones:
- prices_text no vacío y lista resultante no vacía.
- Todos los precios > 0.
- 0 <= discount_rate <= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- Construir la lista de float desde texto.
- En la función, usar un ciclo para crear una nueva lista:
  - discounted_price = price * (1 - discount_rate)
- No modificar la lista de entrada (pure function).
"""
print("Apply Discount to Prices")

def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        discounted.append(new_price)
    return discounted
try:
    prices_text = input("Enter prices separated by commas: ").strip()

    if prices_text == "":
        print("Error: invalid input")
        exit()
    prices_list = []
    for p in prices_text.split(","):
        p = p.strip()
        if p == "":
            print("Error: invalid input")
            exit()
        price_value = float(p)
        if price_value <= 0:
            print("Error: invalid input")
            exit()
        prices_list.append(price_value)
    if len(prices_list) == 0:
        print("Error: invalid input")
        exit()
    discount_rate = float(input("Enter discount rate (0 to 1): "))
    if not (0 <= discount_rate <= 1):
        print("Error: invalid input")
        exit()
    discounted_list = apply_discount(prices_list, discount_rate)
    print(f"Original prices: {prices_list}")
    print(f"Discounted prices: {discounted_list}")
except:
    print("Error: invalid input")

"""

Test Cases

1) Caso Normal
Entrada:
    Enter prices separated by commas: 100, 250, 50
    Enter discount rate (0 to 1): 0.2
Salida esperada:
    Original prices: [100.0, 250.0, 50.0]
    Discounted prices: [80.0, 200.0, 40.0]

2) Caso Borde (descuento = 0 o = 1)
Entrada:
    Enter prices separated by commas: 50, 75
    Enter discount rate (0 to 1): 1
Salida esperada:
    Original prices: [50.0, 75.0]
    Discounted prices: [0.0, 0.0]

3) Caso Error (entrada inválida)
Entrada:
    Enter prices separated by commas: 100, , 300
Salida esperada:
    Error: invalid input
"""
"""
Problema 5. Greeting Function
Descripción:
Define una función greet(name, title="") que:
- Concatene opcionalmente el título antes del nombre (por ejemplo, "Dr. Alice", "Eng. Bob").
- Regrese el mensaje: "Hello, <full_name>!"
Si title está vacío, solo usar el nombre. El código principal debe llamar a la función usando argumentos posicionales y nombrados.

Entradas:
- name (string)
- title (string opcional)

Salidas:
- "Greeting:" <greeting_message>

Validaciones:
- name no vacío tras strip().
- title puede estar vacío, pero si no lo está, también se normaliza con strip().
"""

def greet(name, title=""):
    name = name.strip()
    title = title.strip()
    if name == "":
        return "Error: invalid input"
    if title != "":
        full_name = f"{title} {name}"
    else:
        full_name = name
    return f"Hello, {full_name}!"
name_input = input("Enter name: ").strip()
title_input = input("Enter title (optional): ").strip()

if name_input == "":
    print("Error: invalid input")
else:
    greeting_message = greet(name_input, title_input)
    print("Greeting:", greeting_message)

"""
Test Cases

1) Caso Normal
Entrada:
    Enter name: Alice
    Enter title (optional): Dr.
Salida esperada:
    Greeting: Hello, Dr. Alice!

2) Caso Borde (sin título)
Entrada:
    Enter name: Bob
    Enter title (optional):
Salida esperada:
    Greeting: Hello, Bob!

3) Caso Error (name vacío)
Entrada:
    Enter name:        (solo espacios)
    Enter title (optional): Eng.
Salida esperada:
    Error: invalid input
"""
"""
Problem 6. Factorial
Descripción:
Define una función factorial(n) que regrese n! (n factorial). Puedes implementarla de forma iterativa (con for) o recursiva, pero debes documentar tu elección en comentarios. El código principal debe:
- Leer/definir n.
- Validar n.
- Llamar a factorial(n).
- Mostrar el resultado.

Entradas:
- n (int)

Salidas:
- "n:" <n>
- "Factorial:" <factorial_value>

Validaciones:
- n entero.
- n >= 0.
- Opcional: limitar n a un máximo razonable (por ejemplo n <= 20) para evitar números demasiado grandes; si no se cumple, mostrar "Error: invalid input".
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    n_text = input("Enter a non-negative integer (0 to 20): ").strip()
    if n_text == "":
        print("Error: invalid input")
        exit()
    if not n_text.isdigit():
        print("Error: invalid input")
        exit()
    n = int(n_text)
    if not (0 <= n <= 20):
        print("Error: invalid input")
        exit()
    fact_value = factorial(n)
    print(f"n: {n}")
    print(f"Factorial: {fact_value}")

except:
    print("Error: invalid input")

"""
Test Cases

1) Caso Normal
Entrada:
    Enter a non-negative integer (0 to 20): 5
Salida esperada:
    n: 5
    Factorial: 120

2) Caso Borde (valor mínimo)
Entrada:
    Enter a non-negative integer (0 to 20): 0
Salida esperada:
    n: 0
    Factorial: 1
(Recordar: por definición factorial(0) = 1)

3) Caso Error (fuera de rango)
Entrada:
    Enter a non-negative integer (0 to 20): 25
Salida esperada:
    Error: invalid input
"""
"""
CONCLUSION
Las funciones permiten organizar el programa en partes claras y
reutilizables, evitando repetir código innecesariamente. Devolver
valores con return es útil porque permite usar los resultados en
otros cálculos sin depender solo de impresiones. Los parámetros y
valores por defecto hacen que la función sea más flexible y se
adapte a distintas entradas. Encapsular lógica fue especialmente
cómodo en cálculos repetidos y validaciones. También entendí mejor
la separación entre la lógica principal y las funciones de apoyo,
lo que hace el código más limpio y fácil de modificar.

REFERENCIAS:
1) Python documentation – Defining Functions, parameters and return:
   https://docs.python.org/3/tutorial/controlflow.html#defining-functions
2) Tutoriales de Python sobre funciones y alcance de variables:
   https://realpython.com/defining-your-own-python-function/
3) Libros de algoritmos y programación básica:
   Cormen, Leiserson, Rivest & Stein – "Introduction to Algorithms".
4) Artículos sobre diseño de funciones y buenas prácticas en Python:
   https://realpython.com/python-pep8/
5) Apuntes oficiales de la materia y recursos docentes:
   Universidad Politécnica de Victoria – Material de apoyo de clase.

GitHub Repo Link:
https://github.com/AlejandroVB-23/homeworks_u2.git  
"""