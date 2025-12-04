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