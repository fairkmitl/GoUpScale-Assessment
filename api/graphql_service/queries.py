import graphene
from .types import UserType, ItemType, OrderType
from models.data_utils import USERS, ITEMS, ORDERS


class Query(graphene.ObjectType):
    users = graphene.List(
        UserType,
        sortBy=graphene.String(),
        order=graphene.String(default_value="ASC"),
        limit=graphene.Int(default_value=10),
        offset=graphene.Int(default_value=0),
    )
    user = graphene.Field(UserType, id=graphene.String(required=True))
    user_orders = graphene.List(
        OrderType,
        user_id=graphene.String(required=True),
        sortBy=graphene.String(default_value="order_id"),
        order=graphene.String(default_value="ASC"),
        limit=graphene.Int(default_value=10),
        offset=graphene.Int(default_value=0),
    )
    user_items = graphene.List(ItemType, user_id=graphene.String(required=True))

    def resolve_users(self, info, sortBy=None, order="ASC", limit=10, offset=0):
        sorted_users = USERS

        if sortBy:
            reverse = order == "DESC"
            sorted_users = sorted(
                USERS, key=lambda user: getattr(user, sortBy, None), reverse=reverse
            )

        return sorted_users[offset : offset + limit]

    @staticmethod
    def resolve_user(parent, info, id):
        return next((user for user in USERS if user.id == id), None)

    def resolve_user_orders(
        self, info, user_id, sortBy="order_id", order="ASC", limit=10, offset=0
    ):
        filtered_orders = [order for order in ORDERS if order["user_id"] == user_id]

        reverse = order == "DESC"
        sorted_orders = sorted(
            filtered_orders, key=lambda x: x[sortBy], reverse=reverse
        )

        # Apply pagination using slice
        return sorted_orders[offset : offset + limit]
