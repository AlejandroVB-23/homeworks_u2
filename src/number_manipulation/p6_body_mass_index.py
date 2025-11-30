"""
Problem. 6 Body Mass 
Descripción:
Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
- bmi = weight_kg / (height_m * height_m)
Además, genera booleanos para indicar:
- is_underweight (bmi < 18.5)
- is_normal (18.5 <= bmi < 25.0)
- is_overweight (bmi >= 25.0)

Entradas:
- weight_kg (float; peso en kilogramos).
- height_m (float; estatura en metros).

Salidas:
- "BMI:" <bmi_redondeado>
- "Underweight:" true|false
- "Normal:" true|false
- "Overweight:" true|false

Validaciones:
- weight_kg > 0.0
- height_m > 0.0
- Si no se cumple, mostrar "Error: invalid input".
"""
print("Body Mass Index")
try:
    weight_kg = float(input("Enter your weight in kilograms: "))
    height_m = float(input("Enter your height in meters: "))
    if weight_kg <= 0:
        print("Error Invalid Input")
    elif height_m <= 0:
        print("Error Invalid Input") 
    else:
        bmi = weight_kg / (height_m * height_m)
        is_underweight = (bmi < 18.5)
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0) 
        print(f"BMI: {round(bmi,2)}")
        print(f"Underweight: {is_underweight}")
        print(f"Normal: {is_normal}")
        print(f"Overweight: {is_overweight}")
except:
    print("Error Invalid Input")

"""
# Test Case 1 (Normal):
# Input:
#   weight_kg -> 70
#   height_m  -> 1.75
# Expected Output:
#   BMI: 22.86
#   Underweight: False
#   Normal: True
#   Overweight: False
# (El BMI cae en el rango normal 18.5–24.9)

# Test Case 2 (Borde):
# Input:
#   weight_kg -> 50
#   height_m  -> 1.70
# Expected Output:
#   BMI: 17.30
#   Underweight: True
#   Normal: False
#   Overweight: False
# (Valor bajo, justo en el rango de underweight)

# Test Case 3 (Error):
# Input:
#   weight_kg -> -60
#   height_m  -> 1.80
# Expected Output:
#   Error Invalid Input
# (El peso no puede ser negativo)
"""