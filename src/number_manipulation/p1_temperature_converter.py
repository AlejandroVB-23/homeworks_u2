"""
Problem 1. Temperature Converter
Descripción:
Convierte una temperatura en grados Celsius (float) 
a Fahrenheit y Kelvin. Además, determina un valor booleano 
is_high_temperature que sea true si la temperatura en Celsius es mayor o 
igual que 30.0 y false en caso contrario.

Entradas:
- temp_c (float; temperatura en °C).

Salidas:
- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>
- "High temperature:" true|false

Validaciones:
- Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin 
(por ejemplo, temp_k < 0.0).
"""
print("Temperature converter")
try:
    temp_c = float(input("Enter temperature in Celsius: ")) 
    if not temp_c < -273.15:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c+273.15
        is_high_temperature = temp_c >= 30.0
        print(f"Fahrenheit: {temp_f}")
        print(f"Kelvin: {temp_k}")
        print(f"High temperature: {is_high_temperature}")
    else:
        print("Error: Not Posiible Temperature")
except: 
    print("Enter a valid temperature")

"""
# Test Case 1 (Normal):
# Input:
#   temp_c -> 25
# Expected Output:
#   Fahrenheit: 77.0
#   Kelvin: 298.15
#   High temperature: False
# (25 °C es una temperatura válida y no se considera alta)

# Test Case 2 (Borde):
# Input:
#   temp_c -> -273.15
# Expected Output:
#   Fahrenheit: -459.66999999999996  (equivalente a -459.67 °F)
#   Kelvin: 0.0
#   High temperature: False
# (Justo el límite físico permitido: cero absoluto)

# Test Case 3 (Error):
# Input:
#   temp_c -> -300
# Expected Output:
#   Error: Not Posiible Temperature
# (Temperatura por debajo del cero absoluto)
"""