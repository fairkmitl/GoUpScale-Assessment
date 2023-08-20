### Take home assignment challenge: 
The take home consists of implementing a back_end API serving the data from items.csv, orders.xml and users.json  

The API should be implemented in Python using Flask, GraphQL (graphene library https://graphene-python.org/) and should expose the following on its query:
- A list of users
- A user's details: providing the user-id
- A list of a user's orders: providing the user-id
- A list of items that a user have ordered: providing the user-id

The following mutation should be included:
- User creation: validates input data and creates a user

# Tip: 
- A good separation of concern between API layer and data-fetching layer allows for reusability and a more flexible codebase  
- The data can be re-arranged stored in a different way for optimization purposes when the application starts  

# Bonus:
- Implement sorting and ordering on list APIs (list of users, orders and items)
- Implement pagination on list APIs (list of users, orders and items)
- Implement mutations to add items and orders
- Unit testing
