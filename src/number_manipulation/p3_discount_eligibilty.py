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