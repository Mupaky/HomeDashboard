import datetime
import tkinter


class ReportsScreen(tkinter.Frame):
    def __init__(self, parent, inventory):
        super().__init__(parent)
        self.inventory = inventory
        self.label = None
        self.total_value_label = None
        self.create_widgets()

    def create_widgets(self):
        self.refresh_list()
        self.label = tkinter.Label(self, text="Valuation Report")
        self.label.pack(pady=10)
        self.total_value_label = tkinter.Label(self, text=f"Total Inventory Value:"
                                                          f" ${self.inventory.total_inventory_value():.2f}"
                                                          f" , Date {datetime.datetime.strftime(datetime.datetime.now(), "%c")}")
        self.total_value_label.pack(pady=10)

    def refresh_list(self):
        if self.label is not None:
            self.label.destroy()
            self.total_value_label.destroy()
