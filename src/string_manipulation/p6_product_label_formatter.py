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