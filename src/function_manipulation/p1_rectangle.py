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