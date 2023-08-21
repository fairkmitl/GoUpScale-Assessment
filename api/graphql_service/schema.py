import graphene
from .types import UserType, UserInputType, ItemType, OrderType
from models.data_utils import USERS, ITEMS, ORDERS


class CreateUser(graphene.Mutation):
    class Arguments:
        user_data = UserInputType(required=True)

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(parent, info, user_data):
        from models.data_utils import User, USERS

        new_user = User(**user_data)
        USERS.append(new_user)
        return CreateUser(user=new_user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.String(required=True))
    user_orders = graphene.List(OrderType, user_id=graphene.String(required=True))
    user_items = graphene.List(ItemType, user_id=graphene.String(required=True))

    @staticmethod
    def resolve_users(parent, info):
        return USERS

    @staticmethod
    def resolve_user(parent, info, id):
        return next((user for user in USERS if user.id == id), None)

    @staticmethod
    def resolve_user_orders(parent, info, user_id):
        return [order for order in ORDERS if order.user_id == user_id]

    @staticmethod
    def resolve_user_items(parent, info, user_id):
        orders = [order for order in ORDERS if order.user_id == user_id]
        item_ids = [item_id for order in orders for item_id in order.item_ids]
        return [item for item in ITEMS if item.id in item_ids]


schema = graphene.Schema(query=Query, mutation=Mutation)
