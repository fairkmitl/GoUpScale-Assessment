import graphene
from .types import UserType, ItemType, OrderType
from models.data_utils import USERS, ITEMS, ORDERS


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, userId=graphene.Int(required=True))
    user_orders = graphene.List(OrderType, userId=graphene.Int(required=True))
    user_items = graphene.List(ItemType, userId=graphene.Int(required=True))

    def resolve_users(self, info):
        return USERS

    @staticmethod
    def resolve_user(parent, info, id):
        return next((user for user in USERS if user.id == id), None)

    def resolve_user_orders(self, info, userId):
        return [order for order in ORDERS if order.userId == userId]

    def resolve_user_items(self, info, userId):
        item_ids = []
        for order in ORDERS:
            if order.userId == userId:
                item_ids.extend(order.itemIds)
        return [item for item in ITEMS if item.itemId in item_ids]
