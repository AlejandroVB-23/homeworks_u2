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