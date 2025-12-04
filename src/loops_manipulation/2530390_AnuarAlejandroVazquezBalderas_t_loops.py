"""
Nombre: Anuar Alejandro Vazquez Balderas
Matricula: 2530390
Grupo: 1-1 IM

RESUMEN EJECUTIVO: 
# Un bucle for se usa para recorrer secuencias como listas, rangos o cadenas,
# ejecutando un bloque de código un número determinado de veces. El bucle
# while se emplea cuando una acción debe repetirse mientras una condición
# siga siendo verdadera, lo cual es natural en menús o lecturas repetidas.
# Un contador incrementa valores paso a paso y un acumulador suma resultados
# a lo largo del ciclo. Definir correctamente la condición de salida evita
# ciclos infinitos que pueden bloquear el programa. El documento cubrirá la
# descripción de cada problema, sus entradas y salidas, las validaciones
# necesarias y el uso práctico de for y while en recorridos, cálculos y menús.
"""
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
"""
Problem 2. Multiplication Table
Descripción:
Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta un límite m. Por ejemplo, si base = 5 y m = 4, muestra:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20

Entradas:
- base (int)
- m (int; límite de la tabla)

Salidas:
- Línea por cada multiplicación:
  - "5 x 1 = 5"
  - "5 x 2 = 10"
  - etc.

Validaciones:
- base y m convertibles a int.
- m >= 1; si no, "Error: invalid input".
"""
print("Multiplication Table")
try: 
    base = int(input("Enter the base: "))
    m = int(input("Enter the limit: "))
    if m >= 1:
        for i in range(1,m+1):
            result = i*base
            print(f"{base} x {i}: {result}")
    else: 
        print("Error Invalid Input")
except:
    print("Error Invalid Input")

"""
# Test Case 1 (Normal):
# Input:
# base = 3
# m = 5
# Expected Output:
# 3 x 1: 3
# 3 x 2: 6
# 3 x 3: 9
# 3 x 4: 12
# 3 x 5: 15


# Test Case 2 (Borde):
# Input:
# base = 7
# m = 1
# Expected Output:
# 7 x 1: 7


# Test Case 3 (Error):
# Input:
# base = 4
# m = 0
# Expected Output:
# Error Invalid Input
"""
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
"""
Problem 4. Password Attempts
Descripción:
Implementa un sistema sencillo de intento de contraseña. 
Define en el código una contraseña correcta (por ejemplo, "admin123"). 
El usuario tiene un máximo de MAX_ATTEMPTS intentos para introducirla. 
Si acierta dentro del límite, mostrar un mensaje de éxito. Si agota los 
intentos, mostrar un mensaje de bloqueo.

Entradas:
- user_password (string; se lee en cada intento).

Salidas:
- Si acierta:
  - "Login success"
- Si falla todos los intentos:
  - "Account locked"

Validaciones:
- MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
- Contar correctamente los intentos.
"""
PASSWORD = "admin123"
MAX_ATTEMPTS = 3
attempt = 0
while attempt < MAX_ATTEMPTS:
    user_password = input("Enter the password: ")
    if user_password == PASSWORD:
        print("Login Success")
        break
    else: 
        attempt += 1
        remaining_attempts = MAX_ATTEMPTS-attempt
        if remaining_attempts > 0:
            print(f"Incorrect Password. You have {remaining_attempts} attempts more")
        else: 
            print("Account Locked")

"""
# Test Case 1 (Normal):
# Input:
# Attempt 1: "wrongpass"
# Attempt 2: "admin123"
# Expected Output:
# Incorrect Password. You have 2 attempts more
# Login Success


# Test Case 2 (Borde):
# Input:
# Attempt 1: "wrong1"
# Attempt 2: "wrong2"
# Attempt 3: "wrong3"
# Expected Output:
# Incorrect Password. You have 2 attempts more
# Incorrect Password. You have 1 attempts more
# Account Locked


# Test Case 3 (Error):
# Input:
# Attempt 1: ""
# Attempt 2: ""
# Attempt 3: ""
# Expected Output:
# Incorrect Password. You have 2 attempts more
# Incorrect Password. You have 1 attempts more
# Account Locked
"""
"""
Problem 5. Simple Menu
Descripción:
Implementa un menú de texto que se repite hasta que el usuario 
seleccione la opción de salir. Ejemplo de menú:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
El programa debe ejecutar la acción correspondiente a 
cada opción y volver a mostrar el menú hasta que se elija 0.

Entradas:
- option (string o int; elección del usuario).

Salidas:
- Mensajes según la opción:
  - "Hello!" para saludo.
  - "Counter:" <counter_value> para mostrar contador.
  - "Counter incremented" al incrementar.
  - "Bye!" al salir.
- Para opciones inválidas:
  - "Error: invalid option"

Validaciones:
- Normalizar option (por ejemplo, convertir a int con manejo de error).
- Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.
"""
print("Simple Menu: ")
print("1) Show greeting")
print("2) Show current counter value")
print("3) Increment counter")
counter_value = 0
option = None

while option != 0: 
    try: 
        option = int(input("Enter the option to do: "))
    except: 
        print("Error Invalid Input")
        continue
    if option == 1:
        print("Hello!")
    elif option == 2:
        print(f"Counter {counter_value}")
    elif option == 3:
        counter_value += 1
        print("Counter incremented")
    elif option == 0:
        print("Bye!")
        break
    else:
        print("Error Invalid Option")

"""
# Test Case 1 (Normal):
# Input:
# option = 1
# option = 3
# option = 2
# option = 0
# Expected Output:
# Hello!
# Counter incremented
# Counter 1
# Bye!


# Test Case 2 (Borde):
# Input:
# option = 3
# option = 3
# option = 2
# option = 0
# Expected Output:
# Counter incremented
# Counter incremented
# Counter 2
# Bye!


# Test Case 3 (Error):
# Input:
# option = "abc"
# option = 9
# option = 0
# Expected Output:
# Error Invalid Input
# Error Invalid Option
# Bye!
"""
"""
Problem 6. Tiangle with nested loops
Usa bucles for anidados para imprimir un patrón de asteriscos 
en forma de triángulo rectángulo. Por ejemplo, para n = 4:
*
**
***
****
Además, imprime un segundo patrón invertido (opcional si lo deseas
 extender, pero documenta tu decisión).

Entradas:
- n (int; número de filas del patrón).

Salidas:
- Patrón línea por línea:
  - "*"
  - "**"
  - "***"
  - "****"
- (Opcional) Patrón invertido si se implementa.

Validaciones:
- n convertible a int.
- n >= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- for i in range(1, n + 1):
    - construir una cadena con i asteriscos usando "*" * i
- (Opcional) otro bucle for para el patrón invertido.
"""

print("Paterrn with *")
try:
    n = int(input("Enter number of rows"))
    print("Normal Pattern")
    for i in range(1,n+1):
        row = ""
        for j in range(i):
            row += "*"
        print(row)    
    print("Inverted Pattern:")
    for i in range(n,0,-1):
        row = ""
        for j in range(i):
            row += "*"
        print(row) 
except:
    print("Invalid Input")
"""
# Test Case 1
# Input:
# 3
# Output esperado:
# Normal Pattern
# *
# **
# ***
# Inverted Pattern
# ***
# **
# *

# Test Case 2
# Input:
# 5
# Output esperado:
# Normal Pattern
# *
# **
# ***
# ****
# *****
# Inverted Pattern
# *****
# ****
# ***
# **
# *

# Test Case 3
# Input:
# hola
# Output esperado:
# Invalid Input
"""
"""
CONCLUSION: 
# El for es práctico cuando ya conozco cuántas veces debo repetir una acción,
# mientras que el while funciona mejor cuando la repetición depende de una
# condición que puede cambiar con cada intento. Los contadores y acumuladores
# me ayudaron a llevar control de repeticiones y a sumar valores dentro de un
# ciclo. Con el while existe el riesgo de crear ciclos infinitos si la
# condición nunca cambia o no se actualiza correctamente. Ejemplos comunes
# son los menús interactivos y los intentos de contraseña, donde el programa
# espera hasta que el usuario dé una entrada válida. También aprendí cómo
# funcionan los bucles anidados y cómo pueden generar patrones o tablas
# repitiendo ciclos dentro de otros.

REFERENCIAS:
# 1) Python documentation – “for statements” y “while statements”.
#    https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
#    https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
# 2) W3Schools – Python For Loops y Python While Loops.
#    https://www.w3schools.com/python/python_for_loops.asp
#    https://www.w3schools.com/python/python_while_loops.asp
# 3) Automate the Boring Stuff with Python – A. Sweigart
#    (Capítulos de estructuras de control y ciclos repetitivos).
# 4) Apuntes universitarios de Algoritmos y Programación – Secciones sobre
#    bucles, contadores, acumuladores y control de flujo.
# 5) Artículo: “Design Patterns for Loop Structures” – Conceptos sobre uso
#    de patrones, menús y control mediante condiciones repetitivas.

GitHub Repo Link: 
https://github.com/AlejandroVB-23/homeworks_u2.git   
"""
