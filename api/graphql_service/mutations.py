import graphene
from .types import UserType
from models.data_utils import USERS, User


class CreateUser(graphene.Mutation):
    class Arguments:
        userId = graphene.Int(required=True)
        # Add other fields for User here e.g., name = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, userId, **kwargs):
        # Add validation logic if needed

        user = User(userId=userId, **kwargs)  # Create the user instance
        USERS.append(user)  # Add the user to our in-memory database

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
