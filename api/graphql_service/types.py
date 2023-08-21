import graphene


class UserType(graphene.ObjectType):
    user_id = graphene.String()
    name = graphene.String()
    email = graphene.String()
    age = graphene.Int()


class ItemType(graphene.ObjectType):
    item_id = graphene.String()
    name = graphene.String()
    price = graphene.Float()


class OrderType(graphene.ObjectType):
    order_id = graphene.String()
    user_id = graphene.String()
    item_ids = graphene.List(graphene.String)
