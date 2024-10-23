import tkinter

from models.Inventory import Inventory
from views.AddItemScreen import AddItemScreen
from views.InventoryScreen import InventoryScreen
from views.ReportsScreen import ReportsScreen


class AppController(tkinter.Tk):
    inventory = Inventory()

    def __init__(self):
        super().__init__()
        self.title("Inventory Management")
        self.geometry("800x600")
        self.current_screen = None
        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tkinter.Frame(self)
        self.main_frame.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)

        # Nav left frame
        self.navigation_frame = tkinter.Frame(self, width=200, bg='lightgray')
        self.navigation_frame.pack(side=tkinter.LEFT, fill=tkinter.Y)

        # Buttons creation
        self.inventory_button = tkinter.Button(self.navigation_frame, text="Inventory", command=self.show_inventory_screen)
        self.inventory_button.pack(fill=tkinter.X, padx=5, pady=5)

        self.add_item_button = tkinter.Button(self.navigation_frame, text="Add Item", command=self.show_add_item_screen)
        self.add_item_button.pack(fill=tkinter.X, padx=5, pady=5)

        self.reports_button = tkinter.Button(self.navigation_frame, text="Reports", command=self.show_reports_screen)
        self.reports_button.pack(fill=tkinter.X, padx=5, pady=5)

        # Screens creation
        self.inventory_screen = InventoryScreen(self.main_frame, self.inventory)
        self.add_item_screen = AddItemScreen(self.main_frame, self.inventory)
        self.reports_screen = ReportsScreen(self.main_frame, self.inventory)

        # Attaching Inventory screen to the main frame
        self.show_inventory_screen()

    def show_screen(self, screen):
        if self.current_screen is not None:
            self.current_screen.pack_forget()
        screen.pack(fill=tkinter.BOTH, expand=True)
        self.current_screen = screen

    def show_inventory_screen(self):
        self.inventory_screen.refresh_list()
        self.show_screen(self.inventory_screen)

    def show_add_item_screen(self):
        self.show_screen(self.add_item_screen)

    def show_reports_screen(self):
        self.reports_screen.create_widgets()
        self.show_screen(self.reports_screen)
