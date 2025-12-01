"""
Problem 2. Multiplication Table
Descripción:
Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta un límite m. Por ejemplo, si base = 5 y m = 4, muestra:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20

Entradas:
- base (int)
- m (int; límite de la tabla)

Salidas:
- Línea por cada multiplicación:
  - "5 x 1 = 5"
  - "5 x 2 = 10"
  - etc.

Validaciones:
- base y m convertibles a int.
- m >= 1; si no, "Error: invalid input".
"""
print("Multiplication Table")
try: 
    base = int(input("Enter the base: "))
    m = int(input("Enter the limit: "))
    if m >= 1:
        for i in range(1,m+1):
            result = i*base
            print(f"{base} x {i}: {result}")
    else: 
        print("Error Invalid Input")
except:
    print("Error Invalid Input")

"""
# Test Case 1 (Normal):
# Input:
# base = 3
# m = 5
# Expected Output:
# 3 x 1: 3
# 3 x 2: 6
# 3 x 3: 9
# 3 x 4: 12
# 3 x 5: 15


# Test Case 2 (Borde):
# Input:
# base = 7
# m = 1
# Expected Output:
# 7 x 1: 7


# Test Case 3 (Error):
# Input:
# base = 4
# m = 0
# Expected Output:
# Error Invalid Input
"""