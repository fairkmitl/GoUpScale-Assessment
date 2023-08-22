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
    orderedItems = graphene.List(
        ItemType,
        sortBy=graphene.String(default_value="id"),
        order=graphene.String(default_value="ASC"),
    )

    def resolve_orderedItems(self, info, sortBy="id", order="ASC"):
        print("self.id: ", self.id)
        item_ids = []
        for order in ORDERS:
            if order["user_id"] == self.id:
                item_ids.extend(order["item_ids"])

        # Get the items ordered by the user
        user_items = [item for item in ITEMS if item.id in item_ids]

        # Sort the items
        reverse = order == "DESC"
        return sorted(user_items, key=lambda x: getattr(x, sortBy), reverse=reverse)


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
