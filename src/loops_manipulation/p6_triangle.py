"""
Problem 6. Tiangle with nested loops
Usa bucles for anidados para imprimir un patrón de asteriscos 
en forma de triángulo rectángulo. Por ejemplo, para n = 4:
*
**
***
****
Además, imprime un segundo patrón invertido (opcional si lo deseas
 extender, pero documenta tu decisión).

Entradas:
- n (int; número de filas del patrón).

Salidas:
- Patrón línea por línea:
  - "*"
  - "**"
  - "***"
  - "****"
- (Opcional) Patrón invertido si se implementa.

Validaciones:
- n convertible a int.
- n >= 1; si no, "Error: invalid input".

Operaciones clave sugeridas:
- for i in range(1, n + 1):
    - construir una cadena con i asteriscos usando "*" * i
- (Opcional) otro bucle for para el patrón invertido.
"""

print("Paterrn with *")
try:
    n = int(input("Enter number of rows"))
    print("Normal Pattern")
    for i in range(1,n+1):
        row = ""
        for j in range(i):
            row += "*"
        print(row)    
    print("Inverted Pattern:")
    for i in range(n,0,-1):
        row = ""
        for j in range(i):
            row += "*"
        print(row) 
except:
    print("Invalid Input")
"""
# Test Case 1
# Input:
# 3
# Output esperado:
# Normal Pattern
# *
# **
# ***
# Inverted Pattern
# ***
# **
# *

# Test Case 2
# Input:
# 5
# Output esperado:
# Normal Pattern
# *
# **
# ***
# ****
# *****
# Inverted Pattern
# *****
# ****
# ***
# **
# *

# Test Case 3
# Input:
# hola
# Output esperado:
# Invalid Input
"""