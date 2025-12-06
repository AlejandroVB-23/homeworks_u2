"""
Problem 6. Factorial
Descripción:
Define una función factorial(n) que regrese n! (n factorial). Puedes implementarla de forma iterativa (con for) o recursiva, pero debes documentar tu elección en comentarios. El código principal debe:
- Leer/definir n.
- Validar n.
- Llamar a factorial(n).
- Mostrar el resultado.

Entradas:
- n (int)

Salidas:
- "n:" <n>
- "Factorial:" <factorial_value>

Validaciones:
- n entero.
- n >= 0.
- Opcional: limitar n a un máximo razonable (por ejemplo n <= 20) para evitar números demasiado grandes; si no se cumple, mostrar "Error: invalid input".
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    n_text = input("Enter a non-negative integer (0 to 20): ").strip()
    if n_text == "":
        print("Error: invalid input")
        exit()
    if not n_text.isdigit():
        print("Error: invalid input")
        exit()
    n = int(n_text)
    if not (0 <= n <= 20):
        print("Error: invalid input")
        exit()
    fact_value = factorial(n)
    print(f"n: {n}")
    print(f"Factorial: {fact_value}")

except:
    print("Error: invalid input")

"""
Test Cases

1) Caso Normal
Entrada:
    Enter a non-negative integer (0 to 20): 5
Salida esperada:
    n: 5
    Factorial: 120

2) Caso Borde (valor mínimo)
Entrada:
    Enter a non-negative integer (0 to 20): 0
Salida esperada:
    n: 0
    Factorial: 1
(Recordar: por definición factorial(0) = 1)

3) Caso Error (fuera de rango)
Entrada:
    Enter a non-negative integer (0 to 20): 25
Salida esperada:
    Error: invalid input
"""






