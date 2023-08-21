import graphene
from .types import UserType, ItemType, OrderType
from models.data_utils import USERS, ITEMS, ORDERS


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, user_id=graphene.String(required=True))
    user_orders = graphene.List(OrderType, user_id=graphene.String(required=True))
    user_items = graphene.List(ItemType, user_id=graphene.String(required=True))

    def resolve_users(self, info):
        return USERS

    def resolve_user(self, info, user_id):
        for user in USERS:
            if user.user_id == user_id:
                return user
        return None

    def resolve_user_orders(self, info, user_id):
        return [order for order in ORDERS if order.user_id == user_id]

    def resolve_user_items(self, info, user_id):
        user_order_items = [
            order.item_ids for order in ORDERS if order.user_id == user_id
        ]
        items = []
        for item_list in user_order_items:
            for item_id in item_list:
                for item in ITEMS:
                    if item.item_id == item_id:
                        items.append(item)
        return items
