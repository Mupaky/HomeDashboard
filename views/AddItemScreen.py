import tkinter

from models.Item import Item


class AddItemScreen(tkinter.Frame):
    def __init__(self, parent, inventory):
        super().__init__(parent)
        self.inventory = inventory
        self.create_widgets()

    # Adding Items to Inventory Form
    def create_widgets(self):
        self.form_frame = tkinter.LabelFrame(self, text="Add New Item", padx=15, pady=15)
        self.form_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.name_label = tkinter.Label(self.form_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tkinter.Entry(self.form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.category_label = tkinter.Label(self.form_frame, text="Category:")
        self.category_label.grid(row=1, column=0, padx=5, pady=5)
        self.category_entry = tkinter.Entry(self.form_frame)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        self.quantity_label = tkinter.Label(self.form_frame, text="Quantity:")
        self.quantity_label.grid(row=2, column=0, padx=5, pady=5)
        self.quantity_entry = tkinter.Entry(self.form_frame)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        self.price_label = tkinter.Label(self.form_frame, text="Price per Unit:")
        self.price_label.grid(row=3, column=0, padx=5, pady=5)
        self.price_entry = tkinter.Entry(self.form_frame)
        self.price_entry.grid(row=3, column=1, padx=5, pady=5)

        self.supplier_label = tkinter.Label(self.form_frame, text="Supplier:")
        self.supplier_label.grid(row=4, column=0, padx=5, pady=5)
        self.supplier_entry = tkinter.Entry(self.form_frame)
        self.supplier_entry.grid(row=4, column=1, padx=5, pady=5)

        self.add_button = tkinter.Button(self.form_frame, text="Add Item", command=self.add_item)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_item(self):
        item = Item(
            item_name=self.name_entry.get(),
            category=self.category_entry.get(),
            quantity=int(self.quantity_entry.get()),
            buy_price=float(self.price_entry.get()),
            supplier_name=self.supplier_entry.get())

        if self.inventory.add_item(item):
            print("Item added successfully!")
