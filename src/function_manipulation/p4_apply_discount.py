"""
Problem. Apply Discount List
Descripción:
Define una función apply_discount(prices_list, discount_rate) que:
- reciba una lista de precios (float) y una tasa de descuento (por ejemplo, 0.10 para 10%)
- regrese una nueva lista con los precios ya descontados (no modificar la lista original).
El código principal debe:
- Crear una lista de precios.
- Llamar a la función.
- Mostrar la lista original y la nueva lista con descuento.

Entradas:
- prices_text (string; por ejemplo, "100,200,300")
- discount_rate (float, entre 0 y 1)

Salidas:
- "Original prices:" <original_list>
- "Discounted prices:" <discounted_list>

Validaciones:
- prices_text no vacío y lista resultante no vacía.
- Todos los precios > 0.
- 0 <= discount_rate <= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- Construir la lista de float desde texto.
- En la función, usar un ciclo para crear una nueva lista:
  - discounted_price = price * (1 - discount_rate)
- No modificar la lista de entrada (pure function).
"""
print("Apply Discount to Prices")

def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        discounted.append(new_price)
    return discounted
try:
    prices_text = input("Enter prices separated by commas: ").strip()

    if prices_text == "":
        print("Error: invalid input")
        exit()
    prices_list = []
    for p in prices_text.split(","):
        p = p.strip()
        if p == "":
            print("Error: invalid input")
            exit()
        price_value = float(p)
        if price_value <= 0:
            print("Error: invalid input")
            exit()
        prices_list.append(price_value)
    if len(prices_list) == 0:
        print("Error: invalid input")
        exit()
    discount_rate = float(input("Enter discount rate (0 to 1): "))
    if not (0 <= discount_rate <= 1):
        print("Error: invalid input")
        exit()
    discounted_list = apply_discount(prices_list, discount_rate)
    print(f"Original prices: {prices_list}")
    print(f"Discounted prices: {discounted_list}")
except:
    print("Error: invalid input")

"""

Test Cases

1) Caso Normal
Entrada:
    Enter prices separated by commas: 100, 250, 50
    Enter discount rate (0 to 1): 0.2
Salida esperada:
    Original prices: [100.0, 250.0, 50.0]
    Discounted prices: [80.0, 200.0, 40.0]

2) Caso Borde (descuento = 0 o = 1)
Entrada:
    Enter prices separated by commas: 50, 75
    Enter discount rate (0 to 1): 1
Salida esperada:
    Original prices: [50.0, 75.0]
    Discounted prices: [0.0, 0.0]

3) Caso Error (entrada inválida)
Entrada:
    Enter prices separated by commas: 100, , 300
Salida esperada:
    Error: invalid input
"""