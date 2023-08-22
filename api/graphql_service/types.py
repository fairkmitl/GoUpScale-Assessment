import graphene
from models.data_utils import USERS, ITEMS, ORDERS


class ItemType(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    image_url = graphene.String()
    created_at = graphene.String()


class UserType(graphene.ObjectType):
    id = graphene.String()
    first_name = graphene.String(name="first_name")
    last_name = graphene.String(name="last_name")
    email = graphene.String()
    orderedItems = graphene.List(ItemType)

    def resolve_orderedItems(self, info):
        print("self.id: ", self.id)
        item_ids = []
        for order in ORDERS:
            if order["user_id"] == self.id:
                item_ids.extend(order["item_ids"])

        # This assumes that the items in ITEMS are dictionaries with key 'id'
        return [item for item in ITEMS if item.id in item_ids]


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
