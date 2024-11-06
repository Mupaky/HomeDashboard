import tkinter as tk

from models.Inventory import Inventory
from views.frames.AddItemFrame import AddItemScreen
from views.frames.InventoryFrame import InventoryScreen
from views.frames.ReportsFrame import ReportsScreen
from views.SidebarSubMenu import SidebarSubMenu

selectionbar_color = '#eff5f6'
sidebar_color = '#7a2721'
header_color = '#bf5f58'
visualisation_frame_color = "#ffffff"


class AppController(tk.Tk):
    inventory = Inventory()


    def __init__(self):
        super().__init__()
        self.title("Inventory Management")
        self.geometry("1100x700")
        self.current_screen = None

        self.item_frames = (InventoryScreen,
                   AddItemScreen,
                   ReportsScreen
                   )

        self.create_widgets()



    def create_widgets(self):
        self.header = tk.Frame(self, bg=header_color)
        self.header.place(relx=0.2, rely=0, relwidth=0.8, relheight=0.1)

        self.main_frame = tk.Frame(self)
        self.main_frame.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.9)

        # Nav left frame
        self.sidebar_frame = tk.Frame(self, bg=sidebar_color)
        self.sidebar_frame.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        self.app_name_frame = tk.Frame(self.sidebar_frame, bg=sidebar_color)
        self.app_name_frame.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        logo = tk.Label(self.app_name_frame, bg=sidebar_color)
        logo.place(x=5, y=20)

        uni_name = tk.Label(self.app_name_frame,
                            text='Dashboard',
                            bg=sidebar_color,
                            font=("", 15, "bold")
                            )
        uni_name.place(x=55, y=27, anchor="w")

        uni_name = tk.Label(self.app_name_frame,
                            text='App',
                            bg=sidebar_color,
                            font=("", 15, "bold")
                            )
        uni_name.place(x=55, y=60, anchor="w")

        self.submenu_frame = tk.Frame(self.sidebar_frame, bg=sidebar_color)
        self.submenu_frame.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)

        submenu1 = SidebarSubMenu(self.sidebar_frame,
                                  sub_menu_heading='Option menu',
                                  sub_menu_options=["Inventory",
                                                    "Add Item",
                                                    "Reports",
                                                    ]
                                  )
        submenu1.options["Inventory"].config(
            command=lambda: self.show_frame(InventoryScreen, container)
        )
        submenu1.options["Add Item"].config(
            command=lambda: self.show_frame(AddItemScreen, container)
        )
        submenu1.options["Reports"].config(
            command=lambda: self.show_frame(ReportsScreen, container)
        )

        submenu1.place(relx=0, rely=0.15, relwidth=1, relheight=0.6)

        container = tk.Frame(self)
        container.config(highlightbackground="#808080", highlightthickness=0.5)
        container.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.9)

        self.frames = {}

        for F in self.item_frames:
            frame = F(container, self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.show_frame(InventoryScreen, container)

    def show_frame(self, cont, container):
        del self.frames[cont]
        frame = cont(container, self)
        self.frames[cont] = frame
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        frame.tkraise()
