"""
Problem 5. Password Strength Classifier 

Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según 
reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.).

Entradas:
- password_input (string).

Salidas:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"

Validaciones:
- No aceptar contraseña vacía.
- Verificar longitud con len().
"""
has_upper = False
has_lower = False
has_digit = False
has_symbol = False
print("Password Strength Classifier ")
password_input = input("Enter the password: ").strip()
password_length = len(password_input) >= 8
if not password_input ==  "":
  if len(password_input) > 3:
    for character in password_input:
      if character.isupper():
        has_upper = True
      elif character.islower():
        has_lower = True
      elif character.isdigit():
        has_digit = True
      else:
        has_symbol = True
    if not password_length:
        print("Password strength: weak")
    elif password_length and has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    elif password_length and (
        (has_upper and has_lower) or   
        (has_lower and has_digit) or   
        (has_upper and has_digit)  
    ):
        print("Password strength: medium")
    else:
        print("Password strength: weak")
  else:
    print("The password must contain at least 4 characaters")
else:
   print("No empty entries allowed")