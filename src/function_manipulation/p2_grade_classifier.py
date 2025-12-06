"""
Descripción:
Define una función classify_grade(score) que reciba una calificación numérica (0–100) y regrese una categoría:
- "A" si score >= 90
- "B" si 80 <= score < 90
- "C" si 70 <= score < 80
- "D" si 60 <= score < 70
- "F" si score < 60
El código principal debe llamar la función y mostrar el resultado.

Entradas:
- score (float o int)

Salidas:
- "Score:" <score>
- "Category:" <grade_letter>

Validaciones:
- 0 <= score <= 100
- Si no se cumple, mostrar "Error: invalid input" y no clasificar.
"""
def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
try:
    score_text = input("Enter score (0–100): ").strip()

    if score_text == "":
        print("Error: invalid input")
        exit()
    score = float(score_text)
    if not (0 <= score <= 100):
        print("Error: invalid input")
        exit()
    grade = classify_grade(score)
    print(f"Score: {score}")
    print(f"Category: {grade}")
except:
    print("Error: invalid input")

"""
Test Cases

1) Caso Normal
Entrada:
    Enter score (0–100): 85
Salida esperada:
    Score: 85.0
    Category: B

2) Caso Borde (límite superior de cambio de categoría)
Entrada:
    Enter score (0–100): 90
Salida esperada:
    Score: 90.0
    Category: A

3) Caso Error (fuera de rango)
Entrada:
    Enter score (0–100): 120
Salida esperada:
    Error: invalid input
"""