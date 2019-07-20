from collections import namedtuple
from datetime import date

Order = namedtuple('MyOrder', ['product_name', 'category', 'customer_id', 'due_date', 'model', ])

if __name__ == '__main__':
    order = Order('Keyboard', 'IT', 2, date.today(), 'MK2322')
    print(order)
    print(order.product_name)
    print(order.category)
    print(order.due_date)