
#made EMPL ahead of time in MongoDB. Use the EMPL.txt file and run the code on MongoDB prior to running this example


import pprint
import datetime

# create a MongoClient and connect to local instance
from pymongo import MongoClient
client = MongoClient()

# use the library db in your assignment and/or whatever databases you want
db = client.EMPL
employees = db.employees
daysoff	= db.daysoff


import pprint

pprint.pprint(employees.find_one({"role": "Accountant"}))

for u in employees.distinct("name",
    {"$and":[{"salary": {"$gte": 41000}},
                             {"ranking": {"$lte": 6}},
                             ]}):
    pprint.pprint(u)