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