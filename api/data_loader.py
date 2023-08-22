import csv
import json
import xml.etree.ElementTree as ET


# Loading CSV Data
def load_csv_data(filename):
    with open(filename, newline="") as csvfile:
        return list(csv.DictReader(csvfile))


# Loading JSON Data
def load_json_data(filename):
    with open(filename) as jsonfile:
        return json.load(jsonfile)


# Loading XML Data
def load_xml_data(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    orders = []
    for order in root.findall("order"):
        order_data = {}
        for child in order:
            order_data[child.tag] = child.text
        orders.append(order_data)
    return orders


items = load_csv_data("../data/items.csv")
users = load_json_data("../data/users.json")
orders = load_xml_data("../data/orders.xml")


def get_user_by_id(user_id):
    return next((user for user in users if user["id"] == user_id), None)


def get_orders_by_user_id(user_id):
    return [order for order in orders if order["user_id"] == user_id]


def get_items_by_user_id(user_id):
    user_orders = get_orders_by_user_id(user_id)
    return [
        item
        for order in user_orders
        for item in items
        if item["id"] == order["item_id"]
    ]
