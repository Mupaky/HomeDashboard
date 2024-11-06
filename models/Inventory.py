from dataclasses import dataclass
from models import Item


@dataclass
class Inventory:
    inventory_list: list[Item]

    def __init__(self):
        self.inventory_list = []

    def add_item(self, item):
        se = set(self.inventory_list)
        if not se.__contains__(item):
            item.item_id = len(self.inventory_list) + 1
            self.inventory_list.append(item)
            return True
        return False

    def remove_item(self, id_to_remove: int):
        part = self.is_item(id_to_remove)
        if part:
            self.inventory_list.remove(part)

    def add_quantity(self, id_to_upgrade: int, quantity: int):
        part = self.is_item(id_to_upgrade)
        if part:
            part.quantity += quantity

    def update_quantity(self, id_to_upgrade: int, quantity: int):
        part = self.is_item(id_to_upgrade)
        if part:
            part.quantity = quantity

    def get_list_items(self):
        if not self.inventory_list:
            return "No parts in the inventory"
        else:
            return self.inventory_list

    def total_inventory_value(self):
        return sum(item.quantity * item.buy_price for item in self.inventory_list)

    def is_item(self, id_to_check):
        return next((is_item for is_item in self.inventory_list if is_item.item_id == id_to_check), None)
