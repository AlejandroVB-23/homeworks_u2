"""
Nombre: Anuar Alejandro Vazquez Balderas
Matricula: 2530390
Grupo: 1-1 IM

Resumen Ejecutivo:
Un string en Python es un tipo de dato que almacena texto y es inmutable,
lo que significa que no puede modificarse carácter por carácter.
Permite operaciones como concatenar, medir longitud con len(), extraer
subcadenas con slices y buscar patrones mediante find() o el operador in.
También se puede reemplazar texto con replace() y limpiar espacios con
strip(), además de dividir y unir cadenas con split() y join().
Validar y normalizar texto (correos, nombres o contraseñas) evita errores,
mantiene consistencia en los datos y mejora la seguridad del programa.
El documento explicará cada problema, sus entradas y salidas, las
validaciones aplicadas y el uso de métodos de strings con casos de prueba.
"""
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
"""
Problem 2. Simple Email Validator

Entradas:
- email_text (string).

Salidas:
- "Valid email: true" o "Valid email: false"
- Si es válido: "Domain: <domain_part>"

Validaciones:
- email_text no vacío tras strip().
- Contar cuántas veces aparece '@'.
- Verificar que no haya espacios (no debe haber " " en email_text).
"""
print("Email Validator")
email_text = str(input("Enter your email: ").strip())
split_email = email_text.split()
at_sign_count = email_text.count("@")
at_sign_index = email_text.find("@")
domain_part = email_text[at_sign_index+1:]
valid_email = False

if email_text == "":
    print(f"Valid Email: {valid_email}")
    print("No empty entries allowed")
elif len(split_email) > 1: 
    print(f"Valid Email: {valid_email}")
    print("No whitespaces allowed")
elif not at_sign_count == 1:
    print(f"Valid Email: {valid_email}")
    print("There must be just one '@'" )
elif not "." in domain_part:
    print(f"Valid Email: {valid_email}")
    print("Domain not valid")
else: 
    valid_email = True
    print(f"Valid Email {valid_email}")
    print(f"Domain: {domain_part}")

"""
# Test Case 1 (Normal):
# Input: "usuario@example.com"
# Expected Output:
# Valid Email True
# Domain: example.com

# Test Case 2 (Borde):
# Input: "   john.doe@domain.org   "
# (Con espacios al inicio y final, pero el strip() los elimina)
# Expected Output:
# Valid Email True
# Domain: domain.org

# Test Case 3 (Error):
# Input: "user@@example..com"
# (Tiene más de un '@', por lo que debe fallar)
# Expected Output:
# Valid Email: False
# There must be just one '@'}
"""
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
"""
Problem 4. Sentence word stats

Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).

Entradas:
- sentence (string).

Salidas:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validaciones:
- Oración no vacía tras strip().
- Debe contener al menos una palabra válida después de split().
"""
shortest_word = None
longest_word = None

print("Sentence word stats")
sentence = input("Enter your sentence: ").strip()
if not sentence == "":
   splited_sentence = sentence.split()
   word_count = len(splited_sentence)
   for word in splited_sentence:
      word_length = len(word)
      if shortest_word is None or word_length < len(shortest_word):
         shortest_word = word
      if longest_word is None or word_length > len(longest_word) :
         longest_word = word
   print(f"Word count: {word_count}")
   print(f"First Word: {splited_sentence[0]}")
   print(f"Last Word: {splited_sentence[-1]}")
   print(f"Shortest Word: {shortest_word}")
   print(f"Longest Word: {longest_word}")
else:
   print("No empty entries allowed")

"""
# Test Case 1 (Normal):
# Input: "Python makes coding fun"
# Expected Output:
# Word count: 4
# First Word: Python
# Last Word: fun
# Shortest Word: fun
# Longest Word: Python

# Test Case 2 (Borde):
# Input: "Hola"
# Expected Output:
# Word count: 1
# First Word: Hola
# Last Word: Hola
# Shortest Word: Hola
# Longest Word: Hola

# Test Case 3 (Error):
# Input: ""
# Expected Output:
# No empty entries allowed

"""
"""
Problem 5. Password Strength Classifier 

Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según 
reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).

Entradas:
- password_input (string).

Salidas:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"

Validaciones:
- No aceptar contraseña vacía.
- Verificar longitud con len().
"""
has_upper = False
has_lower = False
has_digit = False
has_symbol = False
print("Password Strength Classifier ")
password_input = input("Enter the password: ").strip()
password_length = len(password_input) >= 8
if not password_input ==  "":
  if len(password_input) > 3:
    for character in password_input:
      if character.isupper():
        has_upper = True
      elif character.islower():
        has_lower = True
      elif character.isdigit():
        has_digit = True
      else:
        has_symbol = True
    if not password_length:
        print("Password strength: weak")
    elif password_length and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    elif password_length and (
        (has_upper and has_lower) or   
        (has_lower and has_digit) or   
        (has_upper and has_digit)  
    ):
        print("Password strength: medium")
    else:
        print("Password strength: weak")
  else:
    print("The password must contain at least 4 characaters")
else:
   print("No empty entries allowed")

"""
# Caso 1: Entrada vacía
# Input: "" 
# Output esperado: "No empty entries allowed"

# Caso 2: Contraseña corta débil
# Input: "Ab1" 
# Output esperado: "The password must contain at least 4 characaters"

# Caso 3: Contraseña fuerte
# Input: "Abc123$%" 
# Output esperado: "Password strength: strong"
"""
"""
Problem 6. Product Label Formatter
Descripción:
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:

Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caracteres.

Entradas:
- product_name (string).
- price_value (puede leerse como string o número; conviértelo a string para mostrarlo).

Salidas:
- "Label: <exactly 30 characters>"
(Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)

Validaciones:
- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.
"""
print("Product Label Formatter")
product_name = input("Enter the product name: ").strip()
if not product_name == "":
    try:
        price_value = float(input("Enter the product value: "))
        label = f"Product: {product_name} | Price: $ {price_value}"
        if price_value >= 0: 
            label_length = len(label)
            if label_length < 30:
                label = label.ljust(30)
                print(f"Label: '{label}' ")
            else: 
                print("Label:", label[:30])
        else:
            print("Enter a valid value")
    except:
        print("Enter a valid value")    
else:
    print("No empty entries allowed")

"""
# Test Case 1 (Normal):
# Input:
#   product_name -> "Pen"
#   price_value  -> 2.0
# Expected Output:
#   Label: 'Product: Pen | Price: $ 2.0       '
# (La etiqueta mide menos de 30 caracteres, por lo que se rellena 
# con espacios a la derecha hasta 30)

# Test Case 2 (Borde):
# Input:
#   product_name -> "Apple"
#   price_value  -> 12.5
# Expected Output:
#   Label: 'Product: Apple | Price: $ 12.5'
# (La etiqueta mide exactamente 30 caracteres, no necesita 
# espacios adicionales ni recorte)

# Test Case 3 (Error):
# Input:
#   product_name -> "Laptop"
#   price_value  -> -1500
# Expected Output:
#   Enter a valid value

"""
"""
CONCLUSION:
 El manejo de strings es esencial en la entrada y salida de datos porque casi
 toda la información del usuario llega como texto y debe procesarse correctamente.
 Funciones como lower(), strip(), split() y join() son útiles para limpiar,
 organizar y estandarizar el texto antes de usarlo en comparaciones o cálculos.
 Normalizar el texto evita inconsistencias, por ejemplo al comparar correos,
 nombres o comandos que podrían escribirse con mayúsculas o espacios extras.
 Un buen diseño de validaciones previene errores, datos basura y comportamientos
 inesperados que afectarían el funcionamiento del programa.
Además, comprendí que los strings son inmutables y que los slices permiten
 extraer partes del texto sin modificar la cadena original.
"""
"""
REFERENCIAS: 
1) Python documentation – Built-in Types: Text Sequence Type — str.
    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
 2) W3Schools – Python Strings Tutorial.
    https://www.w3schools.com/python/python_strings.asp
 3) Automate the Boring Stuff with Python – A. Sweigart (Sección de manejo
    de texto y validación de entradas).
 4) Introducción a la Programación en Python – Apuntes universitarios de
    estructuras básicas y manipulación de cadenas.
 5) Artículo: “Input Validation Best Practices” – OWASP Foundation,
    principios sobre limpieza y normalización de datos de entrada.

GitHub Repo Link: 
https://github.com/AlejandroVB-23/homeworks_u2.git    
"""