from dataclasses import dataclass
import datetime

@dataclass
class Order:
    product_name: str
    category_name: str
    customer_id: int
    due_date: datetime.date


if __name__ == '__main__':
    order = Order('Intel I7', 'IT', '2', datetime.date.today())
    print(order)