items = {}
def create_item(item_id, name, price, quantity):
    if item_id in items:
        print