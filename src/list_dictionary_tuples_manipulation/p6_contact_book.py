"""
Problem 6. Simple Contact Book

Descripción:
Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)
El programa debe:
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
3) Según la acción:
   - "ADD": lee name y phone, agrega o actualiza el contacto.
   - "SEARCH": lee name y muestra el teléfono si existe.
   - "DELETE": lee name y elimina el contacto si existe.
4) Mostrar un mensaje indicando el resultado de la operación.

Entradas:
- action_text (string; "ADD", "SEARCH" o "DELETE").
- name (string; depende de la acción).
- phone (string; solo para "ADD").

Salidas:
- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"

Validaciones:
- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las tres opciones válidas.
- name no vacío tras strip().
- Para "ADD": phone no vacío tras strip().
"""
print("Contact Book")

CONTACT_BOOK = {'JAIME': '12345',
                'ELIAS': '98765',
                'MARIO': '45678',
                }
print(f"Current Contact Book: {CONTACT_BOOK}")
action_text = input("Select an action: ADD/SEARCH/DELETE: ").strip().upper()
if action_text == "":
    print("No empty entries allowed")
elif action_text == "ADD":
    name = input("Enter the new contact: ").strip().upper()
    phone = input("Enter the phone number: ").strip()
    if not name == "" or not phone == "":
       CONTACT_BOOK[name] = phone
       print(f"Contact Saved: {name}, {CONTACT_BOOK[name]}")
       print(f"New Contact Book: {CONTACT_BOOK}")
    else:     
       print("No empty entries allowed")
elif action_text == "SEARCH":
    name = input("Enter the contact to search: ").upper().strip()
    if name == "":
        print("No empty entries allowed")
    elif name in CONTACT_BOOK:
        phone = CONTACT_BOOK.get(name)
        print(f"Phone: {phone}")
    else: 
        print("Error: contact not found")
elif action_text == "DELETE":
    name = input("Enter the contact to delete: ").upper().strip()
    if name == "":
        print("No empty entries allowed")
    elif name in CONTACT_BOOK:
        delated_contact = CONTACT_BOOK.pop(name)
        print(f"Delated Contact: {name}, {delated_contact}")
        print(f"New Contact Book: {CONTACT_BOOK}")
    else:
        print("Error: Contact Not found")
else:
    print("Select a valid option")

"""
# Test Case 1 (Normal - ADD):
# Input:
# action_text = "ADD"
# name = "ANA"
# phone = "11122"
# Expected Output:
# Contact Saved: ANA, 11122
# New Contact Book: {'JAIME': '12345', 'ELIAS': '98765', 'MARIO': '45678', 'ANA': '11122'}


# Test Case 2 (Borde - SEARCH contacto existente):
# Input:
# action_text = "SEARCH"
# name = "MARIO"
# Expected Output:
# Phone: 45678


# Test Case 3 (Error - DELETE contacto inexistente):
# Input:
# action_text = "DELETE"
# name = "PEDRO"
# Expected Output:
# Error: Contact Not found
"""