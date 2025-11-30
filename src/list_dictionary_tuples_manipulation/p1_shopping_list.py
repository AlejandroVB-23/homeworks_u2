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