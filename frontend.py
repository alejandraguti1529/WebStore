from Product import Product 
from DAO import get, insert, delete, update


menu = """

Welcome to the WebStore.

Choose an option.

1 - Insert product
2 - See all
3 - Update
4 - Delete
5 - Exit

"""

eleccion = None

while eleccion is not 5:
    print(menu)
    eleccion = int(input("Choose: "))
    if eleccion is 1:
        print("Insert")
        name = raw_input("Product name: ")
        description = raw_input("Product description: ")
        quantity = int(raw_input("Product quantity: "))
        product = Product(name, description, quantity)
        id = insert(product)
        print("The id of the inserted product is: ", id)
    elif eleccion is 2:
        print("Obtaining products ...")
        for product in get():
            print("=================")
            print("Id: ", product["_id"])
            print("Name: ", product["name"])
            print("Description: ", product["description"])
            print("quatity: ", product["quantity"])
    elif eleccion is 3:
        print("Update")
        id = raw_input("Write the id: ")
        name = raw_input("New product name: ")
        description = raw_input("New product description: ")
        quantity = float(raw_input("New product quantity: "))
        product = Product(name, description, quantity)
        updated_products = update(id, product)
        print("Number of updated products: ", updated_products)
    elif eleccion is 4:
        print("delete")
        id = raw_input("Write the id: ")
        products_deleted = delete(id)
        print("Number of products removed:", products_deleted)