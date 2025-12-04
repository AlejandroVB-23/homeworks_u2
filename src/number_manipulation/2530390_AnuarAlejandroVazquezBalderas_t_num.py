"""
Nombre: Anuar Alejandro Vazquez Balderas
Matricula: 2530390
Grupo: 1-1 IM

RESUMEN EJECUTIVO:
 En Python, los tipos int y float representan números: int para valores
# enteros sin decimales y float para valores con parte decimal. La diferencia
# principal es la precisión y el uso en operaciones que requieren números
# reales. Un booleano (True/False) expresa un valor lógico y normalmente se
# obtiene al realizar comparaciones como >, <, == o >=. Validar rangos evita
# cálculos inválidos, y comprobar que no exista división entre cero previene
# errores que detienen el programa. El documento incluirá la descripción de
# cada problema, el diseño de sus entradas y salidas, las validaciones
# necesarias y el uso de enteros, flotantes y booleanos para tomar decisiones.
"""
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

"""
Problem 2. Work Hours and Overtime Payment

Descripción:
Calcula el pago total semanal de un trabajador. Hasta 40 horas s
e pagan a hourly_rate (float). Las horas extra (> 40) se pagan 
al 150% de la tarifa normal. Además, genera un booleano has_overtime
 que indique si el trabajador hizo horas extra.

Entradas:
- hours_worked (float; horas trabajadas en la semana).
- hourly_rate (float; pago por hora).

Salidas:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false

Validaciones:
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".
"""
print("Work Hours and Overtime Payment")
try:
    hours_worked = float(input("Enter the hours worked: "))
    hourly_rate = float(input("Enter the hourly rate: "))
    if hours_worked >= 0 and hourly_rate > 0:
        has_overtime = hours_worked > 40
        regular_hours = min(hours_worked,40)
        extra_hours = max(hours_worked-40,0)
        regular_pay = regular_hours*hourly_rate
        overtime_pay = extra_hours*(hourly_rate*1.5)
        total_pay = regular_pay+overtime_pay
        print(f"Regular Pay: {regular_pay}")
        print(f"Overtime Pay: {overtime_pay}")
        print(f"Total Pay: {total_pay}")
        print(f"Has Overtime: {has_overtime}")
    else:
        print("Error: Invalid Input")
except:
    print("Enter valid data")

"""
# Test Case 1 (Normal):
# Input:
#   hours_worked -> 45
#   hourly_rate  -> 20
# Expected Output:
#   Regular Pay: 800.0          
#   Overtime Pay: 150.0         
#   Total Pay: 950.0
#   Has Overtime: True
# (Trabajó más de 40 horas, así que recibe pago extra)

# Test Case 2 (Borde):
# Input:
#   hours_worked -> 40
#   hourly_rate  -> 15
# Expected Output:
#   Regular Pay: 600.0          
#   Overtime Pay: 0.0
#   Total Pay: 600.0
#   Has Overtime: False
# (Exactamente 40 horas: no hay horas extra)

# Test Case 3 (Error):
# Input:
#   hours_worked -> -5
#   hourly_rate  -> 10
# Expected Output:
#   Error: Invalid Input
# (Las horas no pueden ser negativas)
"""
"""
Problem 3. Discount Eligibility
Descripción:
Determina si un cliente obtiene un descuento en su compra. La regla es:
- Tiene descuento si:
  - is_student es true OR
  - is_senior es true OR
  - purchase_total >= 1000.0
Calcula también el total a pagar aplicando un 10% de 
descuento cuando sea elegible.

Entradas:
- purchase_total (float; total de la compra).
- is_student_text (string; "YES" o "NO").
- is_senior_text (string; "YES" o "NO").

Salidas:
- "Discount eligible:" true|false
- "Final total:" <final_total>

Validaciones:
- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir 
a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".
"""
print("Discount Eligibility")
try:
    purchase_total = float(input("Enter your total purchase: "))
    is_student_text = input("Are you student?: ").strip().upper()
    is_senior_text = input("Are you senior?: ").strip().upper()
    if purchase_total <= 0.0:
        print("Error: Invalid Input")
    elif (is_student_text not in ("YES", "NO") or 
        is_senior_text not in ("YES", "NO")):
        print("Error: invalid input")
    else:
        is_student = (is_student_text == "YES")
        is_senior = (is_senior_text == "YES")
        discount_eligible = (
            is_student or
            is_senior or
            purchase_total >= 1000.0)
        if discount_eligible:
            final_total = purchase_total * 0.9    
        else:
            final_total = purchase_total
        print(f"Discount eligible: {discount_eligible}")
        print(f"Final total: {final_total}")
except:
    print("Enter valid data")

"""
# Test Case 1 (Normal):
# Input:
#   purchase_total -> 1200
#   is_student_text -> "NO"
#   is_senior_text  -> "NO"
# Expected Output:
#   Discount eligible: True
#   Final total: 1080.0
# (Es elegible porque la compra supera $1000)

# Test Case 2 (Borde):
# Input:
#   purchase_total -> 1000
#   is_student_text -> "YES"
#   is_senior_text  -> "NO"
# Expected Output:
#   Discount eligible: True
#   Final total: 900.0
# (Aunque está justo en el límite, es estudiante, por lo tanto aplica descuento)

# Test Case 3 (Error):
# Input:
#   purchase_total -> -50
#   is_student_text -> "YES"
#   is_senior_text  -> "NO"
# Expected Output:
#   Error: Invalid Input
# (El total de compra no puede ser negativo)
"""
"""
Problem 4. Basic statistics of three integers
Descripción:
Lee tres números enteros y calcula: suma, promedio (float), 
valor máximo, valor mínimo y un booleano all_even que indique
 si los tres números son pares.

Entradas:
- n1 (int)
- n2 (int)
- n3 (int)

Salidas:
- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false

Validaciones:
- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).
"""
print("Basic statistics of three integers")
try: 
    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    n3 = int(input("Number 3: "))
    sum_value = n1+n2+n3
    average_value = sum_value/3
    max_value = max(n1,n2,n3)
    min_value = min(n1,n2,n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    print(f"Sum: {sum_value}") 
    print(f"Average: {average_value}") 
    print(f"Max: {max_value}") 
    print(f"Min: {min_value}")
    print(f"All Even: {all_even}")
except: 
    print("All numbers must be integers")

"""
Test Cases:
1) Caso de prueba: todos pares
#    Entrada:
#       Number 1: 4
#       Number 2: 10
#       Number 3: 6
#    Salida esperada:
#       Sum: 20
#       Average: 6.6666666667
#       Max: 10
#       Min: 4
#       All Even: True
#
# 2) Caso de prueba: mezcla de positivos y negativos
#    Entrada:
#       Number 1: -3
#       Number 2: 7
#       Number 3: 1
#    Salida esperada:
#       Sum: 5
#       Average: 1.6666666667
#       Max: 7
#       Min: -3
#       All Even: False
#
# 3) Caso de prueba: entrada inválida
#    Entrada:
#       Number 1: 5
#       Number 2: hola
#       Number 3: 8
#    Salida esperada:
#       All numbers must be integers
"""
"""
Problem 5. Loan eligibility
Descripción:
Determina si una persona es elegible para un préstamo con base en:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
La regla es:
- debt_ratio = monthly_debt / monthly_income
- eligible es true si:
  - monthly_income >= 8000.0 AND
  - debt_ratio <= 0.4 AND
  - credit_score >= 650

Entradas:
- monthly_income (float; ingreso mensual).
- monthly_debt (float; pagos mensuales de deuda).
- credit_score (int; puntaje de crédito).

Salidas:
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false

Validaciones:
- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0
- credit_score >= 0
- Si no se cumple, mostrar "Error: invalid input".
"""

print("Loan Eligibility")
try:
    monthly_income = float(input("Enter your monhtly income: "))
    monthly_debt = float(input("Enter your monhtly debt: "))
    credit_score = int(input("Enter your credit score: "))
    if monthly_income <= 0:
        print("Error: Invalid Input")
    elif monthly_debt < 0.0:
        print("Error: Invalid Input")
    elif credit_score < 0: 
        print("Error: Invalid Input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and 
                    debt_ratio <= 0.4 and 
                    credit_score >= 650)
        print(f"Debt Ratio: {debt_ratio}")
        print(f"Eligible: {eligible}")
except:
    print("Error: Invalid Input")

"""
# Test Case 1 (Normal):
# Input:
#   monthly_income -> 10000
#   monthly_debt   -> 2000
#   credit_score   -> 700
# Expected Output:
#   Debt Ratio: 0.2
#   Eligible: True
# (Cumple los tres requisitos: buen ingreso, bajo ratio y buen crédito)

# Test Case 2 (Borde):
# Input:
#   monthly_income -> 8000
#   monthly_debt   -> 3200
#   credit_score   -> 650
# Expected Output:
#   Debt Ratio: 0.4
#   Eligible: True
# (Todos los valores están exactamente en el límite permitido)

# Test Case 3 (Error):
# Input:
#   monthly_income -> -5000
#   monthly_debt   -> 1000
#   credit_score   -> 700
# Expected Output:
#   Error: Invalid Input
# (No se aceptan ingresos negativos)
"""
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
"""
CONCLUSION: 
# Los enteros y flotantes se combinan en la mayoría de cálculos reales, pues
# muchos procesos requieren cantidades exactas junto con valores decimales.
# Las comparaciones producen booleanos que permiten decidir qué camino seguir
# en un programa mediante estructuras if. Validar rangos y evitar divisiones
# entre cero es crucial para prevenir errores y resultados inválidos. También
# aprendí cómo diseñar condiciones más complejas usando and, or y not para
# controlar mejor los casos especiales. Estos patrones se repiten en problemas
# como nóminas, descuentos, cálculos financieros y préstamos, donde las reglas
# dependen de comparaciones y operaciones numéricas.
"""
"""
REFERENCIAS:
# 1) Python documentation – Numeric Types (int, float, complex) y Boolean type.
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
#    https://docs.python.org/3/library/stdtypes.html#boolean-values
# 2) W3Schools – Python Numbers y Python Booleans.
#    https://www.w3schools.com/python/python_numbers.asp
#    https://www.w3schools.com/python/python_booleans.asp
# 3) Automate the Boring Stuff with Python – A. Sweigart (Capítulos de
#    operadores, condiciones y validación).
# 4) Apuntes universitarios de Algoritmos y Programación – Secciones de tipos
#    numéricos, operadores lógicos y diseño de condiciones.
 5) Artículo: “Input Validation Techniques for Numeric Data” – Buenas
    prácticas para validar rangos, evitar errores y asegurar consistencia.

GitHub Repo Link: 
https://github.com/AlejandroVB-23/homeworks_u2.git    
"""