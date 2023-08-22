import graphene
from .types import UserType, UserInputType, ItemType, OrderType
from .queries import Query


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


schema = graphene.Schema(query=Query, mutation=Mutation)
