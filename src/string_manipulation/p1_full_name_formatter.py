"""
Problem 1. Full Name Formatter

Descripcion: Dado el nombre completo de una persona 
en una sola cadena (por ejemplo: "juan carlos tovar"), 
el programa debe:
1) Normalizar el texto (strip, espacios extra
, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case
 y las iniciales (por ejemplo: J.C.T.).

Entradas: full_name
Salidas: formatted_name, initials

Validaciones:
- full_name no debe estar vacío después de strip().
- Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
- No aceptar cadenas que sean solo espacios.
"""

initials = ""
full_name = (str(input("Enter your name: ").strip()).lower())
split_name = full_name.title().split()
formatted_name = " ".join(split_name)
if not full_name == "" and not len(split_name)<2:
    for name in split_name:
        initials += name[0] + "."
    print(f"Formated Name: {formatted_name}")
    print(f"Initials: {initials}")
else: 
    print("Wrong Format")

"""
Test Cases
# Test Case 1 (Normal):
# Input: "Juan Carlos Osorio"
# Expected Output:
# Formated Name: Juan Carlos Osorio
# Initials: J.C.O.

# Test Case 2 (Borde):
# Input: "   maria     lopez    "
# Expected Output:
# Formated Name: Maria Lopez
# Initials: M.L.

# Test Case 3 (Error):
# Input: "Juan" 
# Expected Output:
# Wrong Format
"""
