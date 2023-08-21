import json
import os
import csv
import xml.etree.ElementTree as ET
from .data_models import User, Item, Order

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_users():
    USERS_PATH = os.path.join(BASE_DIR, "../../data/users.json")

    with open(USERS_PATH, "r") as file:
        users_data = json.load(file).values()
        return [User(**user) for user in users_data]


def load_items():
    ITEMS_PATH = os.path.join(BASE_DIR, "../../data/items.csv")

    items = []
    with open(ITEMS_PATH, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(Item(**row))
    return items


def load_orders():
    ORDERS_PATH = os.path.join(BASE_DIR, "../../data/orders.xml")

    tree = ET.parse(ORDERS_PATH)
    root = tree.getroot()

    orders = []
    for order in root.findall("./orders/order"):  # Only select <order> elements
        order_data = {
            "order_id": order.get("id"),
            "user_id": order.find("user_id").text.strip(),
            "item_ids": [
                item.text.strip() for item in order.findall("./items/item/id")
            ],
        }
        orders.append(Order(**order_data))
    return orders


USERS = load_users()
ITEMS = load_items()
ORDERS = load_orders()
