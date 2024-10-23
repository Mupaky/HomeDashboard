from dataclasses import dataclass
from models import Item


@dataclass
class Inventory:
    inventory_list: list[Item]

    def __init__(self):
        self.inventory_list = []

    # Adding Item to the inventory
    def add_item(self, item):
        se = set(self.inventory_list)
        if not se.__contains__(item):
            item.item_id = len(self.inventory_list) + 1
            self.inventory_list.append(item)
            return True
        return False

    # Remove Item from the inventory
    def remove_item(self, id_to_remove: int):
        part = self.is_item(id_to_remove)
        if part:
            self.inventory_list.remove(part)

    # Adding quantity to an item
    def add_quantity(self, id_to_upgrade: int, quantity: int):
        part = self.is_item(id_to_upgrade)
        if part:
            part.quantity += quantity

    # Update/change the quantity of an item
    def update_quantity(self, id_to_upgrade: int, quantity: int):
        part = self.is_item(id_to_upgrade)
        if part:
            part.quantity = quantity

    # Return list of the current items
    def get_list_items(self):
        if not self.inventory_list:
            return "No parts in the inventory"
        else:
            return self.inventory_list

    # Calculate the total value of the items in the inventory
    def total_inventory_value(self):
        return sum(item.quantity * item.buy_price for item in self.inventory_list)

    # Check if the items by id {id_to_check} exist in the inventory and return it otherwise returns null/None
    def is_item(self, id_to_check):
        return next((is_item for is_item in self.inventory_list if is_item.item_id == id_to_check), None)
