"""
Order - basic
"""
from datetime import timedelta
from datetime import date

class Order:
    def __init__(self, product_name, category, customer_id):
        self.product_name = product_name
        self.category = category
        self.customer_id = customer_id
        self.due = None


    @property
    def due_date(self):
        return self.due

    @due_date.setter
    def due_date(self, due):
        if due < date.today():
            return False
        self.due = due

if __name__ == "__main__":
    order = Order(
        'Keyboard',
        'IT',
        1,
    )
    print(order)
    print(order.product_name, order.due_date)
    order.due_date = date.today() - timedelta(days=1)
