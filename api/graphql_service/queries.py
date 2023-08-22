import graphene
from .types import UserType, ItemType, OrderType
from models.data_utils import USERS, ITEMS, ORDERS


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.String(required=True))
    user_orders = graphene.List(OrderType, user_id=graphene.String())
    user_items = graphene.List(
        ItemType, user_id=graphene.String(required=True)
    )  # consistent with user_id

    def resolve_users(self, info):
        return USERS

    @staticmethod
    def resolve_user(parent, info, id):
        return next((user for user in USERS if user.id == id), None)

    # @staticmethod
    def resolve_user_orders(parent, info, user_id):
        # print("user_id : ", user_id)
        # print("All ORDERS:", ORDERS)
        filtered_orders = [order for order in ORDERS if order["user_id"] == user_id]
        # print(f"Filtered orders for user {user_id}: {filtered_orders}")
        return filtered_orders
