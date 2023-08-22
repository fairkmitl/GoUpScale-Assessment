import graphene


class UserType(graphene.ObjectType):
    id = graphene.String()
    first_name = graphene.String(name="first_name")
    last_name = graphene.String(name="last_name")
    email = graphene.String()


class ItemType(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    image_url = graphene.String()
    created_at = graphene.String()


class OrderType(graphene.ObjectType):
    order_id = graphene.String()
    user_id = graphene.String()
    item_ids = graphene.List(graphene.String)


class UserInputType(graphene.InputObjectType):
    id = graphene.String()
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String(required=True)
