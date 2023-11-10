import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['example_database']

collection = db['users']

user_data = [
    {"name": "Kobi", "age": 25},
    {"name": "Jeremy", "age": 29},
    {"name": "Jonz", "age": 30}
]
result = collection.insert_many(user_data)
print("Inserted IDs:", result.inserted_ids)

all_users = collection.find()
print("\nAll Users:")
for user in all_users:
    print(user)

query = {"name": "Kobi"}
new_values = {"$set": {"age": 26}}
collection.update_one(query, new_values)
print("\nUser 'Kobi' updated.")

query = {"name": "Kobi"}
new_values = {"$set": {"name": "Kobe"}}
collection.update_one(query, new_values)

print("\nUser 'Kobi' modified to 'Kobe'.")
all_users_after_update = collection.find()
print("\nAll Users After Update:")
for user in all_users_after_update:
    print(user)


query = {"name": "Kobe"}
collection.delete_one(query)
print("\nUser 'Kobe' deleted.")
all_users_after_deletion = collection.find()
print("\nAll Users After Deletion:")
for user in all_users_after_deletion:
    print(user)