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

