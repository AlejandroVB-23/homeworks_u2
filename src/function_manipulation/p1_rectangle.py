"""
Problem 1: Rectangle area and perimeter
Descripción:
Define dos funciones:
- calculate_area(width, height): regresa el área de un rectángulo.
- calculate_perimeter(width, height): regresa el perímetro.
El código principal debe leer (o definir) los valores, llamar a las 
funciones y mostrar los resultados.

Entradas:
- width (float)
- height (float)

Salidas:
- "Area:" <area_value>
- "Perimeter:" <perimeter_value>

Validaciones:
- width > 0
- height > 0
- Si alguna condición no se cumple, mostrar "Error: invalid input" y 
no llamar a las funciones.
"""

def calculate_area(w, h):
  area_value = w*h
  return area_value
def calculate_perimeter(w,h):
  perimeter_value = 2*(w+h)
  return perimeter_value

try: 
  width = float(input("Enter the width: "))
  height = float(input("Enter the height: "))

  if not width == 0 or not height == 0:
    print(f"Area: {calculate_area(width,height)}")
    print(f"Perimeter: {calculate_perimeter(width,height)}")
  else:
    print("Error Invalid Input")
except:
  print("Error Invalid Input")

"""
Test Cases

1) Caso Normal
Entrada:
    Enter the width: 5
    Enter the height: 3
Salida esperada:
    Area: 15.0
    Perimeter: 16.0

2) Caso Borde (uno de los valores = 0, debería marcar error
pero el código actual NO lo detecta por el uso incorrecto del if)
Entrada:
    Enter the width: 0
    Enter the height: 4
Salida esperada lógica esperada:
    Error Invalid Input
Salida real del programa:
    Area: 0.0
    Perimeter: 8.0

3) Caso Error (entrada no numérica)
Entrada:
    Enter the width: hola
    Enter the height: 5
Salida esperada:
    Error Invalid Input
"""