"""
Nombre: Anuar Alejandro Vazquez Balderas
Matricula: 2530390
Grupo: 1-1 IM

RESUMEN EJECUTIVO:
# En Python, una lista, una tupla y un diccionario son estructuras para
# almacenar múltiples datos: la lista es mutable, la tupla es inmutable
# y el diccionario organiza información mediante pares clave–valor.
# La mutabilidad de las listas permite agregar, borrar o modificar
# elementos, mientras que las tuplas permanecen fijas después de crearse.
# Los diccionarios se usan para acceder rápidamente a información asociada
# a una clave, ideal para registros, catálogos o estadísticas.
# El documento incluirá la descripción de cada problema, el diseño de
# entradas y salidas y las validaciones necesarias.
# También mostrará el uso práctico de listas, tuplas y diccionarios en
# tareas como almacenar datos, buscar valores o estructurar información.
"""
"""
Problem 1. Shopping List
Trabaja con una lista de productos (strings) y sus cantidades (enteros). 
El programa debe:
1) Crear una lista inicial de productos.
2) Permitir agregar un nuevo producto al final.
3) Mostrar la cantidad total de elementos en la lista.
4) Verificar si un producto específico está en la lista 
(booleano is_in_list).

Entradas:
- initial_items_text (string; por ejemplo, "apple,banana,orange").
- new_item (string; producto a agregar).
- search_item (string; producto a buscar).

Salidas:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validaciones:
- initial_items_text no vacío tras strip().
- Separar la cadena por comas y eliminar espacios extra en cada elemento.
- new_item y search_item no vacíos.
- Manejar el caso de lista inicial vacía si el 
estudiante lo decide (documentar decisión).
"""
print("Shopping List Basics")
initial_items_text = input("Enter your initiall items: ").strip().lower() 
new_item = input("Enter the new item: ").strip().lower()
search_item = input("Enter the item to search: ").lower().strip()

if not (initial_items_text == "" or new_item == "" or search_item == ""):
    items_list = initial_items_text.split(",")
    items_list.append(new_item)
    len_list = len(items_list)
    found_item = search_item in items_list
    print(f"Items List {items_list}")
    print(f"Total Items {len_list}")
    print(f"Found Item: {found_item}")
else:
    print("No empty entries allowed")

"""
# Test Case 1 (Normal):
# initial_items_text: "pan,leche,huevos"
# new_item: "queso"
# search_item: "leche"
# items_list -> ['pan', 'leche', 'huevos', 'queso']
# len_list -> 4
# found_item -> True
# Expected Output:
# Items List ['pan', 'leche', 'huevos', 'queso']
# Total Items 4
# Found Item: True


# Test Case 2 (Borde):
# initial_items_text: "pan,leche,huevos"
# new_item: "mantequilla"
# search_item: "jamon"
# items_list -> ['pan', 'leche', 'huevos', 'mantequilla']
# len_list -> 4
# found_item -> False
# Expected Output:
# Items List ['pan', 'leche', 'huevos', 'mantequilla']
# Total Items 4
# Found Item: False


# Test Case 3 (Error):
# initial_items_text: ""
# new_item: "pan"
# search_item: "pan"
# Expected Output:
# No empty entries allowed
"""
""" 
Problem 2: Points and distances with tuples
Descripción:
Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
2) Calcular la distancia euclidiana entre ambos puntos.
3) Crear una nueva tupla midpoint con el punto medio entre ellos.

Entradas:
- x1, y1, x2, y2 (float; coordenadas de los puntos).

Salidas:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Validaciones:
- Verificar que las 4 entradas se puedan convertir a float.
- No se requieren restricciones adicionales en el rango.
"""
print("Points and distances")
try: 
    x1 = float(input("Enter coordinate x1: "))
    y1 = float(input("Enter coordinate y1: "))
    x2 = float(input("Enter coordinate x2: "))
    y2 = float(input("Enter coordinate y2: "))
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    mx = (x1 + x2)/2
    my = (y1 + y2)/2
    midpoint = (mx,my)
    point_a = (x1, y1)
    point_b = (x2, y2)
    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance}")
    print(f"Midpoint: {midpoint}")
except:
    print("Error Invalid Input")

"""
Test Cases 
# 1) Caso normal con números enteros
# Input:
#   x1 = 0
#   y1 = 0
#   x2 = 3
#   y2 = 4
# Output esperado:
#   Point A: (0.0, 0.0)
#   Point B: (3.0, 4.0)
#   Distance: 5.0
#   Midpoint: (1.5, 2.0)

# 2) Caso con números decimales
# Input:
#   x1 = 1.2
#   y1 = -2.5
#   x2 = 4.8
#   y2 = 3.1
# Output esperado:
#   Point A: (1.2, -2.5)
#   Point B: (4.8, 3.1)
#   Distance: 6.589....
#   Midpoint: (3.0, 0.3)

# 3) Caso de error (entrada inválida)
# Input:
#   x1 = hola
#   y1 = 5
#   x2 = 2
#   y2 = 3
# Output esperado:
#   Error Invalid Input
"""
"""
Problem 3. Product Catalog
Descripción:
Administra un pequeño catálogo de productos usando un diccionario donde:
- clave: nombre del producto (string)
- valor: precio unitario (float)
El programa debe:
1) Crear un diccionario inicial con al menos 3 productos.
2) Leer el nombre de un producto y la cantidad a comprar.
3) Calcular el total a pagar si el producto existe.
4) Si el producto no existe, mostrar un mensaje de error.

Entradas:
- product_name (string).
- quantity (int; cantidad a comprar).

Salidas:
- Si el producto existe:
  - "Unit price:" <unit_price>
  - "Quantity:" <quantity>
  - "Total:" <total_price>
- Si el producto no existe:
  - "Error: product not found"

Validaciones:
- quantity > 0.
- product_name no vacío tras strip().
- Verificar si product_name está en el diccionario (clave).
"""
PRODUCT_PRICES = {'apple':4, 'book': 15, 'chair': 45}
try: 
    product_name = input("Enter the product: ").strip().lower()
    quantity = int(input("Enter the quantity: "))
    if product_name == "": 
        print("Enter a valid product")
    elif product_name not in PRODUCT_PRICES:
        print("Product not found")
    elif quantity <= 0:
        print("Enter a valid quantity")
    else: 
        total_price = quantity*PRODUCT_PRICES[product_name] 
        print(f"Unit Price: {PRODUCT_PRICES[product_name]}")
        print(f"Quantity: {quantity}")
        print(f"Total Price: {total_price}")
except:
    print("Enter a valid quantity")

"""
# Test Case 1 (Normal):
# Input:
# product_name = "apple"
# quantity = 3
# total_price -> 3 * 4 = 12
# Expected Output:
# Unit Price: 4
# Quantity: 3
# Total Price: 12


# Test Case 2 (Borde):
# Input:
# product_name = "book"
# quantity = 1
# total_price -> 1 * 15 = 15
# Expected Output:
# Unit Price: 15
# Quantity: 1
# Total Price: 15


# Test Case 3 (Error - producto no existe):
# Input:
# product_name = "laptop"
# quantity = 2
# Expected Output:
# Product not found
"""
"""
Problem 4: Student grades with dict and list
Descripción:
Administra las calificaciones de un grupo usando un diccionario:
- clave: nombre del estudiante (string)
- valor: lista de calificaciones (list of float)
El programa debe:
1) Crear un diccionario con al menos 3 estudiantes, cada 
uno con una lista de calificaciones.
2) Leer el nombre de un estudiante.
3) Calcular el promedio de sus calificaciones.
4) Indicar si el estudiante está aprobado (average >= 70.0) 
con un booleano is_passed.

Entradas:
- student_name (string).

Salidas:
- Si el estudiante existe:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- Si el estudiante no existe:
  - "Error: student not found"

Validaciones:
- student_name no vacío tras strip().
- Verificar si student_name es una clave en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de 
calcular el promedio.
"""
print("Student Grades")
GRADES = {
    'jaime':[94.6,85.0,79.4,66.9],
    'pepe':[84.1,74.9,],
    'kris':[90.2,89.5,100.0]
}
student_name = input("Enter the student name: ").strip().lower()
if student_name == "":
    print("Enter a valid name")
elif student_name not in GRADES:
    print("Error: Student not found")
else: 
    grades_list = GRADES[student_name]  
    if len(grades_list) == 0:
        print("Error: grades no available" )
    else: 
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0
        print(f"Grades: {grades_list}")
        print(f"Average: {average}")
        print(f"Passed: {is_passed}")

"""
# Test Case 1 (Normal):
# Input:
# student_name = "jaime"
# grades_list -> [94.6, 85.0, 79.4, 66.9]
# average -> (94.6 + 85.0 + 79.4 + 66.9) / 4 = 81.475
# is_passed -> True (promedio >= 70)
# Expected Output:
# Grades: [94.6, 85.0, 79.4, 66.9]
# Average: 81.475
# Passed: True


# Test Case 2 (Borde):
# Input:
# student_name = "pepe"
# grades_list -> [84.1, 74.9]
# average -> (84.1 + 74.9) / 2 = 79.5
# is_passed -> True
# Expected Output:
# Grades: [84.1, 74.9]
# Average: 79.5
# Passed: True


# Test Case 3 (Error):
# Input:
# student_name = "marcos"
# Expected Output:
# Error: Student not found
"""
"""
Problem 5: Word frequency counter

Descripción:
Cuenta la frecuencia de cada palabra en una oración usando:
- Una lista de palabras.
- Un diccionario donde:
  - clave: palabra (string)
  - valor: frecuencia (int)
El programa debe:
1) Leer una oración.
2) Convertirla a minúsculas y separarla en una lista de palabras.
3) Construir un diccionario de frecuencias.
4) Mostrar el diccionario completo y la palabra más frecuente.

Entradas:
- sentence (string).

Salidas:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word> (si hay empate, cualquier una es válida)

Validaciones:
- sentence no vacía tras strip().
- Manejar signos de puntuación simples si el estudiante decide hacerlo 
(documentar su decisión, por ejemplo usando replace()).
- Verificar que la lista de palabras no esté vacía.

Operaciones clave sugeridas:
- lower(), split()
- Recorrer la lista y actualizar el diccionario:
  - if word in freq_dict: freq_dict[word] += 1
  - else: freq_dict[word] = 1
- Uso de un ciclo para encontrar la palabra con mayor frecuencia.
"""
print("Problem 5: Word frequency counter")
sentence = input("Enter your sentence: ").lower()
if not sentence == "":
  words_list = sentence.split()
  freq_dict = {}
  for word in words_list:
    if word in freq_dict:
      freq_dict[word] += 1
    else:
      freq_dict[word] = 1
  highest_freq = None
  for word in freq_dict:
    if highest_freq == None or freq_dict[word] > highest_freq:
      highest_freq = freq_dict[word]
      most_common_word = word

  print(f"Words list: {words_list}")
  print(f"Frequencies: {freq_dict}")
  print(f"Most common word: {most_common_word}")
else:
    print("No empty entries allowed")

"""
# Test Case 1 (Normal):
# Input:
# sentence = "the dog chased the cat"
# words_list -> ['the', 'dog', 'chased', 'the', 'cat']
# freq_dict -> {'the': 2, 'dog': 1, 'chased': 1, 'cat': 1}
# most_common_word -> "the"
# Expected Output:
# Words list: ['the', 'dog', 'chased', 'the', 'cat']
# Frequencies: {'the': 2, 'dog': 1, 'chased': 1, 'cat': 1}
# Most common word: the


# Test Case 2 (Borde):
# Input:
# sentence = "hello"
# words_list -> ['hello']
# freq_dict -> {'hello': 1}
# most_common_word -> "hello"
# Expected Output:
# Words list: ['hello']
# Frequencies: {'hello': 1}
# Most common word: hello


# Test Case 3 (Error):
# Input:
# sentence = ""
# Expected Output:
# No empty entries allowed
"""
"""
Problem 6. Simple Contact Book

Descripción:
Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)
El programa debe:
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
3) Según la acción:
   - "ADD": lee name y phone, agrega o actualiza el contacto.
   - "SEARCH": lee name y muestra el teléfono si existe.
   - "DELETE": lee name y elimina el contacto si existe.
4) Mostrar un mensaje indicando el resultado de la operación.

Entradas:
- action_text (string; "ADD", "SEARCH" o "DELETE").
- name (string; depende de la acción).
- phone (string; solo para "ADD").

Salidas:
- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"

Validaciones:
- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las tres opciones válidas.
- name no vacío tras strip().
- Para "ADD": phone no vacío tras strip().
"""
print("Contact Book")

CONTACT_BOOK = {'JAIME': '12345',
                'ELIAS': '98765',
                'MARIO': '45678',
                }
print(f"Current Contact Book: {CONTACT_BOOK}")
action_text = input("Select an action: ADD/SEARCH/DELETE: ").strip().upper()
if action_text == "":
    print("No empty entries allowed")
elif action_text == "ADD":
    name = input("Enter the new contact: ").strip().upper()
    phone = input("Enter the phone number: ").strip()
    if not name == "" or not phone == "":
       CONTACT_BOOK[name] = phone
       print(f"Contact Saved: {name}, {CONTACT_BOOK[name]}")
       print(f"New Contact Book: {CONTACT_BOOK}")
    else:     
       print("No empty entries allowed")
elif action_text == "SEARCH":
    name = input("Enter the contact to search: ").upper().strip()
    if name == "":
        print("No empty entries allowed")
    elif name in CONTACT_BOOK:
        phone = CONTACT_BOOK.get(name)
        print(f"Phone: {phone}")
    else: 
        print("Error: contact not found")
elif action_text == "DELETE":
    name = input("Enter the contact to delete: ").upper().strip()
    if name == "":
        print("No empty entries allowed")
    elif name in CONTACT_BOOK:
        delated_contact = CONTACT_BOOK.pop(name)
        print(f"Delated Contact: {name}, {delated_contact}")
        print(f"New Contact Book: {CONTACT_BOOK}")
    else:
        print("Error: Contact Not found")
else:
    print("Select a valid option")

"""
# Test Case 1 (Normal - ADD):
# Input:
# action_text = "ADD"
# name = "ANA"
# phone = "11122"
# Expected Output:
# Contact Saved: ANA, 11122
# New Contact Book: {'JAIME': '12345', 'ELIAS': '98765', 'MARIO': '45678', 'ANA': '11122'}


# Test Case 2 (Borde - SEARCH contacto existente):
# Input:
# action_text = "SEARCH"
# name = "MARIO"
# Expected Output:
# Phone: 45678


# Test Case 3 (Error - DELETE contacto inexistente):
# Input:
# action_text = "DELETE"
# name = "PEDRO"
# Expected Output:
# Error: Contact Not found
"""
"""
CONCLUSION:
# Las listas son convenientes cuando se necesita almacenar datos que pueden
# crecer, cambiar o eliminarse con frecuencia. Su flexibilidad permite añadir,
# quitar o modificar elementos de forma dinámica. Las tuplas son ideales para
# información fija, como coordenadas, configuraciones o valores que no deben
# alterarse accidentalmente. Los diccionarios destacan por permitir búsquedas
# rápidas mediante claves, facilitando el manejo de registros o catálogos.
# Al combinar estas estructuras observé patrones comunes como diccionarios
# que contienen listas para organizar grupos de elementos, o listas de
# diccionarios para manejar colecciones de registros más complejos.

GitHub Repo Link: 
https://github.com/AlejandroVB-23/homeworks_u2.git   
"""