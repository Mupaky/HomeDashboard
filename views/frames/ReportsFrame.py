import tkinter as tk
import datetime

class ReportsScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text='Reports', font=("Arial", 15))
        label.pack()
        self.controller = controller
        self.label = None
        self.total_value_label = None
        self.create_widgets()

    def create_widgets(self):
        self.refresh_list()
        self.label = tk.Label(self, text="Valuation Report")
        self.label.pack(pady=10)
        self.total_value_label = tk.Label(self, text=f"Total Inventory Value:"
                                                          f" ${self.controller.inventory.total_inventory_value():.2f}"
                                                          f" , Date {datetime.datetime.strftime(datetime.datetime.now(), "%c")}")
        self.total_value_label.pack(pady=10)

    def refresh_list(self):
        if self.label is not None:
            self.label.destroy()
            self.total_value_label.destroy()

