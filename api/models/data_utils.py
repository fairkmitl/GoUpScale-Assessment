import json
from .data_models import User, Item, Order


def load_users():
    with open("../data/users.json", "r") as file:
        users_data = json.load(file)
    return [User(**user) for user in users_data]


import csv


def load_items():
    items = []
    with open("../data/items.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(Item(**row))
    return items


import xml.etree.ElementTree as ET


def load_orders():
    tree = ET.parse("../data/orders.xml")
    root = tree.getroot()

    orders = []
    for order in root:
        order_data = {
            "order_id": order.find("order_id").text,
            "user_id": order.find("user_id").text,
            "item_ids": [item.text for item in order.findall("item_ids/item")],
        }
        orders.append(Order(**order_data))
    return orders


USERS = load_users()
ITEMS = load_items()
ORDERS = load_orders()
