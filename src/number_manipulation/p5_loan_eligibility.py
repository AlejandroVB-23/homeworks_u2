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