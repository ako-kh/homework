from pymongo import MongoClient
import random


client = MongoClient("localhost", 27017)

db = client["products"]
products = db["products"]

my_data = []
categories = ["Electronics", "Books", "Clothes"]
for i in range(1, 50):
    quantity = random.randint(0, 100)
    my_data.append(
        {
            "name": f"Product{i}",
            "category": random.choice(categories),
            "price": random.randint(50, 3000),
            "quantity": quantity,
            "available": quantity > 0
        }
    )
# print(my_data)

products.insert_many(my_data)

for p in products.find():
    print(p)

for p in products.find({"available": True}):
    print(p)

for p in products.find({"price": {"$gt": 1000}}):
    print(p)

pipeline = [
    {
        "$group": {
            "_id": "$category",
            "count": {"$sum": 1}
        }
    }
]

for p in products.aggregate(pipeline):
    print(p)

products.update_one({"name": "Product3"}, {"$set": {"quantity": 4}})
