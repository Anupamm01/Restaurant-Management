class Order:

    def __init__(self):
        self.items = {}    # key item obj and value quantity

    def add_item(self,item,quantity):
        if item in self.items:
            self.items[item] += quantity
            item.quantity -= quantity
        else:
            self.items[item] = quantity
            item.quantity -= quantity

    def remove(self,item):
        if item in self.items:
            del self.items[item]
    @property
    def total_price(self):
        return sum([item.price * quantity for item,quantity in self.items.items()])
    
    def clear(self):
        self.items = {}