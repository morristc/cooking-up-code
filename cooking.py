from pymongo import MongoClient

try:
    conn = MongoClient()
    print("Connected Successfully")
except:
    print("Could not connect")
    
db = conn.database

collection = db.mydatabase

recipe1 = {
    "country": "Ireland",
    "eid": 1,
    "recipe": "Winning Apple Crisp",
    "meal_type": "dessert"
    }
    
recipe2 = {
    "country": "Ireland",
    "eid": 2,
    "recipe": "Stout and Shiitake Pot Roast",
    "meal_type": "entre"
    }
    
recipe3 = {
    "country": "Ireland",
    "eid": 3,
    "recipe": "Colcannon Irish Potatoes",
    "meal_type": "side"
    }
    
rec_id1 = collection.insert_one(recipe1)
rec_id2 = collection.insert_one(recipe2)
rec_id3 = collection.insert_one(recipe3)
 
print("Data inserted with record ids", rec_id1, " ", rec_id2, " ", rec_id3)
 
cursor = collection.find()
for record in cursor:
   print(record)