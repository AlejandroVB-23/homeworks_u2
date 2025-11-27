"""
Problem 2. Simple Email Validator

Entradas:
- email_text (string).

Salidas:
- "Valid email: true" o "Valid email: false"
- Si es válido: "Domain: <domain_part>"

Validaciones:
- email_text no vacío tras strip().
- Contar cuántas veces aparece '@'.
- Verificar que no haya espacios (no debe haber " " en email_text).
"""
print("Email Validator")
email_text = str(input("Enter your email: ").strip())
split_email = email_text.split()
at_sign_count = email_text.count("@")
at_sign_index = email_text.find("@")
domain_part = email_text[at_sign_index+1:]
valid_email = False

if email_text == "":
    print(f"Valid Email: {valid_email}")
    print("No empty entries allowed")
elif len(split_email) > 1: 
    print(f"Valid Email: {valid_email}")
    print("No whitespaces allowed")
elif not at_sign_count == 1:
    print(f"Valid Email: {valid_email}")
    print("There must be just one '@'" )
elif not "." in domain_part:
    print(f"Valid Email: {valid_email}")
    print("Domain not valid")
else: 
    valid_email = True
    print(f"Valid Email {valid_email}")
    print(f"Domain: {domain_part}")

"""
# Test Case 1 (Normal):
# Input: "usuario@example.com"
# Expected Output:
# Valid Email True
# Domain: example.com

# Test Case 2 (Borde):
# Input: "   john.doe@domain.org   "
# (Con espacios al inicio y final, pero el strip() los elimina)
# Expected Output:
# Valid Email True
# Domain: domain.org

# Test Case 3 (Error):
# Input: "user@@example..com"
# (Tiene más de un '@', por lo que debe fallar)
# Expected Output:
# Valid Email: False
# There must be just one '@'}
"""