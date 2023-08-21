import graphene


class UserType(graphene.ObjectType):
    id = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    password = (
        graphene.String()
    )  # Note: For security purposes, avoid exposing the password field in your GraphQL API.


class ItemType(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    image_url = graphene.String()
    created_at = graphene.String()  # This can be changed to DateTime if needed.


class OrderType(graphene.ObjectType):
    order_id = graphene.String()
    user_id = graphene.String()
    item_ids = graphene.List(graphene.String)  # List of item IDs
