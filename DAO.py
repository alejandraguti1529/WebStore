from connection import get_db
from bson.objectid import ObjectId
def get():
    db = get_db()
    return db.products.find()

def insert(product):
    db = get_db()
    products = db.products
    return products.insert_one({
        "name": product.name,
        "description": product.description,
        "quantity": product.quantity,
        }).inserted_id

def delete(id):
    db = get_db()
    result = db.products.delete_one(
        {
        '_id': ObjectId(id)
        })
    return result.deleted_count

def update(id, product):
    db = get_db()
    result = db.products.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
                "name": product.name,
                "description": product.description,
                "quantity": product.quantity,
            }
        })
    return result.modified_count    