import datetime
from dataclasses import dataclass


@dataclass
class Item:
    item_name: str
    category: str
    supplier_name: str
    item_id: int = 0
    quantity: int = 0
    date_added: datetime.datetime = datetime.datetime.now()
    description: str = ""
    buy_price: float = 0.0
    sell_price: float = 0.0

    def __eq__(self, other):
        return (self.item_name == other.item_name and self.category == other.category and
                self.supplier_name == other.supplier_name and self.buy_price == other.buy_price and
                self.sell_price == other.sell_price)

    def __hash__(self):
        return hash((self.item_name, self.category, self.supplier_name, self.buy_price, self.sell_price))

