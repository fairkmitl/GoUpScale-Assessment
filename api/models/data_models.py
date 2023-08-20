# data_models.py


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        # Add other fields if needed


class Item:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price
        # Add other fields if needed


class Order:
    def __init__(self, order_id, user_id, item_ids):
        self.order_id = order_id
        self.user_id = user_id
        self.item_ids = item_ids  # This can be a list of item_ids
        # Add other fields if needed
