"""
Problem 4: Student grades with dict and list
Descripción:
Administra las calificaciones de un grupo usando un diccionario:
- clave: nombre del estudiante (string)
- valor: lista de calificaciones (list of float)
El programa debe:
1) Crear un diccionario con al menos 3 estudiantes, cada 
uno con una lista de calificaciones.
2) Leer el nombre de un estudiante.
3) Calcular el promedio de sus calificaciones.
4) Indicar si el estudiante está aprobado (average >= 70.0) 
con un booleano is_passed.

Entradas:
- student_name (string).

Salidas:
- Si el estudiante existe:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- Si el estudiante no existe:
  - "Error: student not found"

Validaciones:
- student_name no vacío tras strip().
- Verificar si student_name es una clave en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de 
calcular el promedio.
"""
print("Student Grades")
GRADES = {
    'jaime':[94.6,85.0,79.4,66.9],
    'pepe':[84.1,74.9,],
    'kris':[90.2,89.5,100.0]
}
student_name = input("Enter the student name: ").strip().lower()
if student_name == "":
    print("Enter a valid name")
elif student_name not in GRADES:
    print("Error: Student not found")
else: 
    grades_list = GRADES[student_name]  
    if len(grades_list) == 0:
        print("Error: grades no available" )
    else: 
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0
        print(f"Grades: {grades_list}")
        print(f"Average: {average}")
        print(f"Passed: {is_passed}")

"""
# Test Case 1 (Normal):
# Input:
# student_name = "jaime"
# grades_list -> [94.6, 85.0, 79.4, 66.9]
# average -> (94.6 + 85.0 + 79.4 + 66.9) / 4 = 81.475
# is_passed -> True (promedio >= 70)
# Expected Output:
# Grades: [94.6, 85.0, 79.4, 66.9]
# Average: 81.475
# Passed: True


# Test Case 2 (Borde):
# Input:
# student_name = "pepe"
# grades_list -> [84.1, 74.9]
# average -> (84.1 + 74.9) / 2 = 79.5
# is_passed -> True
# Expected Output:
# Grades: [84.1, 74.9]
# Average: 79.5
# Passed: True


# Test Case 3 (Error):
# Input:
# student_name = "marcos"
# Expected Output:
# Error: Student not found
"""