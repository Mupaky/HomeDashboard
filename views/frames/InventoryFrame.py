import tkinter as tk


class InventoryScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Inventory', font=("Arial", 15))
        label.pack()
        self.listbox = None
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for item in self.controller.inventory.inventory_list:
            self.listbox.insert(tk.END, f"ID: {item.item_id}, Name: {item.item_name}, Quantity: {item.quantity}")
