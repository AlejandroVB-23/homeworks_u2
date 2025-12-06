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