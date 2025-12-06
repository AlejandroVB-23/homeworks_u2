"""
Nombre: Anuar Alejandro Vazquez Balderas
Matricula: 2530390
Grupo: 1-1 IM

Resumen Ejecutivo:
Un CRUD es un sistema básico de gestión de datos donde Create agrega,
Read consulta, Update modifica y Delete elimina información almacenada.
Elegí usar un diccionario porque permite acceder rápidamente a cada
elemento mediante su clave única, evitando búsquedas repetitivas.
El uso de funciones hace que cada operación esté separada y clara,
lo que mejora la organización y evita duplicar lógica en el menú.
Mi programa cubre el menú principal, la creación de nuevos registros,
su lectura individual, la actualización de datos, su eliminación y
también el listado completo de los elementos guardados.
"""
def create_item(items, item_id, name, price, quantity):
    """Crea un nuevo item si el id no existe. Regresa True/False."""
    for item in items:
        if item["id"] == item_id:
            return False  
    new_item = {
        "id": item_id,
        "name": name,
        "price": price,
        "quantity": quantity,
    }
    items.append(new_item)
    return True

def read_item(items, item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    return None

def update_item(items, item_id, new_name, new_price, new_quantity):
    for item in items:
        if item["id"] == item_id:
            item["name"] = new_name
            item["price"] = new_price
            item["quantity"] = new_quantity
            return True
    return False

def delete_item(items, item_id):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            del items[index]
            return True
    return False

def list_items(items):
    if not items:
        print("Items list: (empty)")
        return

    print("Items list:")
    for item in items:
        print(
            f"- id: {item['id']}, "
            f"name: {item['name']}, "
            f"price: {item['price']}, "
            f"quantity: {item['quantity']}"
        )

def print_menu():
    print("\n--- CRUD MENU ---")
    print("1) Create item")
    print("2) Read item by id")
    print("3) Update item by id")
    print("4) Delete item by id")
    print("5) List all items")
    print("0) Exit")
def main():
    items = [] 
    while True:
        print_menu()
        option = input("Enter option: ").strip()
        if option == "0":
            print("Exiting program...")
            break
        elif option == "1":
            try:
                item_id = input("Enter item id: ").strip()
                name = input("Enter item name: ").strip()
                price_text = input("Enter price (>= 0): ").strip()
                quantity_text = input("Enter quantity (>= 0): ").strip()
                if item_id == "" or name == "":
                    print("Error: invalid input")
                    continue
                price = float(price_text)
                quantity = int(quantity_text)
                if price < 0 or quantity < 0:
                    print("Error: invalid input")
                    continue
                if create_item(items, item_id, name, price, quantity):
                    print("Item created")
                else:
                    print("Error: id already exists")
            except:
                print("Error: invalid input")
        elif option == "2":
            item_id = input("Enter item id to read: ").strip()
            if item_id == "":
                print("Error: invalid input")
                continue
            item = read_item(items, item_id)
            if item is None:
                print("Item not found")
            else:
                print("Item found:")
                print(
                    f"id: {item['id']}, "
                    f"name: {item['name']}, "
                    f"price: {item['price']}, "
                    f"quantity: {item['quantity']}"
                )
        elif option == "3":
            try:
                item_id = input("Enter item id to update: ").strip()
                if item_id == "":
                    print("Error: invalid input")
                    continue
                new_name = input("Enter new name: ").strip()
                new_price_text = input("Enter new price (>= 0): ").strip()
                new_quantity_text = input(
                    "Enter new quantity (>= 0): "
                ).strip()
                if new_name == "":
                    print("Error: invalid input")
                    continue
                new_price = float(new_price_text)
                new_quantity = int(new_quantity_text)
                if new_price < 0 or new_quantity < 0:
                    print("Error: invalid input")
                    continue
                if update_item(
                    items, item_id, new_name, new_price, new_quantity
                ):
                    print("Item updated")
                else:
                    print("Item not found")
            except:
                print("Error: invalid input")
        elif option == "4":
            item_id = input("Enter item id to delete: ").strip()
            if item_id == "":
                print("Error: invalid input")
                continue
            if delete_item(items, item_id):
                print("Item deleted")
            else:
                print("Item not found")
        elif option == "5":
            list_items(items)
        else:
            print("Error: invalid input")
if __name__ == "__main__":
    main()

"""
CONCLUSION:
El uso de funciones permitió separar cada operación del CRUD, lo cual
hizo el código más claro y evitó repetir lógica en el menú principal.
La lista de diccionarios facilitó almacenar varios registros y acceder
a sus campos sin estructuras complejas. La validación de entradas fue
el mayor reto, especialmente al manejar valores vacíos o no numéricos,
pero se solucionó con try/except y verificaciones explícitas de rango.
Este CRUD podría crecer hacia un sistema más completo guardando datos
en archivos JSON o CSV, o incluso conectándolo a una base de datos
para permitir persistencia y consultas más avanzadas.

REFERENCIAS: 
1) Python documentation – Data structures (dict, list):
   https://docs.python.org/3/tutorial/datastructures.html
2) Python documentation – Defining functions (def, parameters, return):
   https://docs.python.org/3/tutorial/controlflow.html#defining-functions
3) Tutoriales sobre CRUD básico en memoria con Python:
   https://realpython.com/python-data-structures/

GitHub Repo Link:
https://github.com/AlejandroVB-23/homeworks_u2.git
"""