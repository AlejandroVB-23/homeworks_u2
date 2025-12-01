"""
Problem 4. Password Attempts
Descripción:
Implementa un sistema sencillo de intento de contraseña. 
Define en el código una contraseña correcta (por ejemplo, "admin123"). 
El usuario tiene un máximo de MAX_ATTEMPTS intentos para introducirla. 
Si acierta dentro del límite, mostrar un mensaje de éxito. Si agota los 
intentos, mostrar un mensaje de bloqueo.

Entradas:
- user_password (string; se lee en cada intento).

Salidas:
- Si acierta:
  - "Login success"
- Si falla todos los intentos:
  - "Account locked"

Validaciones:
- MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
- Contar correctamente los intentos.
"""
PASSWORD = "admin123"
MAX_ATTEMPTS = 3
attempt = 0
while attempt < MAX_ATTEMPTS:
    user_password = input("Enter the password: ")
    if user_password == PASSWORD:
        print("Login Success")
        break
    else: 
        attempt += 1
        remaining_attempts = MAX_ATTEMPTS-attempt
        if remaining_attempts > 0:
            print(f"Incorrect Password. You have {remaining_attempts} attempts more")
        else: 
            print("Account Locked")

"""
# Test Case 1 (Normal):
# Input:
# Attempt 1: "wrongpass"
# Attempt 2: "admin123"
# Expected Output:
# Incorrect Password. You have 2 attempts more
# Login Success


# Test Case 2 (Borde):
# Input:
# Attempt 1: "wrong1"
# Attempt 2: "wrong2"
# Attempt 3: "wrong3"
# Expected Output:
# Incorrect Password. You have 2 attempts more
# Incorrect Password. You have 1 attempts more
# Account Locked


# Test Case 3 (Error):
# Input:
# Attempt 1: ""
# Attempt 2: ""
# Attempt 3: ""
# Expected Output:
# Incorrect Password. You have 2 attempts more
# Incorrect Password. You have 1 attempts more
# Account Locked
"""

