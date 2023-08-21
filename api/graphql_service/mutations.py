import graphene
from .types import UserType
from models.data_utils import USERS, User


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        age = graphene.Int(required=True)

    user = graphene.Field(lambda: UserType)

    def mutate(self, info, name, email, age):
        user = User(user_id=str(len(USERS) + 1), name=name, email=email, age=age)
        USERS.append(user)
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
