class Order:
    def __init__(self, customer_name, order_date, quantity, contents, order_id):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.contents = contents
        self.order_id = order_id