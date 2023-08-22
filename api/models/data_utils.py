import json
import os
import csv
import xml.etree.ElementTree as ET
from .data_models import User, Item, Order

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Load user data from the users.json file.
def get_element_text(element, tag_name):
    child_element = element.find(tag_name)
    return child_element.text.strip() if child_element is not None else None


def load_users():
    USERS_PATH = os.path.join(BASE_DIR, "../../data/users.json")

    with open(USERS_PATH, "r") as file:
        users_data = json.load(file).values()
        return [User(**user) for user in users_data]


# Load item data from the items.csv file.
def load_items():
    ITEMS_PATH = os.path.join(BASE_DIR, "../../data/items.csv")

    items = []
    with open(ITEMS_PATH, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(Item(**row))
    return items


# Load order data from the orders.xml file.
def load_orders():
    ORDERS_PATH = os.path.join(BASE_DIR, "../../data/orders.xml")
    tree = ET.parse(ORDERS_PATH)
    root = tree.getroot()

    orders = []

    # Use a manual index for looping since we want to access subsequent nodes.
    children = list(
        root.findall("orders/*")
    )  # This gets all child nodes (both order and items)
    index = 0
    while index < len(children):
        child = children[index]
        if child.tag == "order":
            order_data = {
                "order_id": child.get("id"),
                "user_id": get_element_text(child, "user_id"),
                "item_ids": [],
            }

            # Check if the next node is 'items' for this order
            if index + 1 < len(children) and children[index + 1].tag == "items":
                items_element = children[index + 1]
                order_data["item_ids"] = [
                    item.find("id").text.strip()
                    for item in items_element.findall("item")
                ]

                # Increment the index to skip the 'items' node next time
                index += 1

            orders.append(order_data)
        index += 1

    return orders


USERS = load_users()
ITEMS = load_items()
ORDERS = load_orders()
