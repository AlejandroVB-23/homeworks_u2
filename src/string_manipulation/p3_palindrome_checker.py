"""
Problem 3. Palindrome Checker

Descripción:
Determina si una frase es un palíndromo, es decir, 
se lee igual de izquierda a derecha y de derecha a izquierda, 
ignorando espacios y mayúsculas/minúsculas.

Ejemplos:
- "Anita lava la tina" -> palíndromo.
- "Hola mundo" -> no palíndromo.

Entradas:
- phrase (string).

Salidas:
- "Is palindrome: true" o "Is palindrome: false"
- (Opcional) Mostrar también la versión normalizada de la frase.

Validaciones:
- phrase no vacía tras strip().
- Longitud mínima razonable después de limpiar espacios 
(por ejemplo, al menos 3 caracteres).
"""
print("Palindrome Checker")
phrase = input("Enter your phrase: ").strip().lower()
replaced_phrase = phrase.replace(" ", "")
reversed_phrase = replaced_phrase[::-1]
if len(replaced_phrase) < 3:
    print("The phrase must contain at least three characters")
else:
    print(f"Is palindrome: {reversed_phrase==replaced_phrase}")

"""
# Test Case 1 (Normal):
# Input: "anita lava la tina"
# Expected Output:
# Is palindrome: True

# Test Case 2 (Borde):
# Input: "oso"
# Expected Output:
# Is palindrome: True

# Test Case 3 (Error):
# Input: "hi"
# Expected Output:
# The phrase must contain at least three characters
"""