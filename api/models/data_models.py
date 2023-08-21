class User:
    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class Item:
    def __init__(self, id, name, image_url, created_at):
        self.id = id
        self.name = name
        self.image_url = image_url
        self.created_at = created_at


class Order:
    def __init__(self, order_id, user_id, item_ids):
        self.order_id = order_id
        self.user_id = user_id
        self.item_ids = item_ids
