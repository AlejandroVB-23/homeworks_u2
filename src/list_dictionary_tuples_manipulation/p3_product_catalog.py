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


# Test Case 4 (Error - cantidad inválida):
# Input:
# product_name = "chair"
# quantity = 0
# Expected Output:
# Enter a valid quantity


# Test Case 5 (Error - entrada no numérica):
# Input:
# product_name = "apple"
# quantity = "xyz"
# Expected Output:
# Enter a valid quantity
"""