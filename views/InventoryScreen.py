import tkinter


class InventoryScreen(tkinter.Frame):
    def __init__(self, parent, inventory):
        super().__init__(parent)
        self.listbox = None
        self.inventory = inventory
        self.create_widgets()

    def create_widgets(self):
        self.listbox = tkinter.Listbox(self)
        self.listbox.pack(fill=tkinter.BOTH, expand=True)
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tkinter.END)
        for item in self.inventory.inventory_list:
            self.listbox.insert(tkinter.END, f"ID: {item.item_id}, Name: {item.item_name}, Quantity: {item.quantity}")
