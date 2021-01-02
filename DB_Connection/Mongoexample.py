from pymongo import MongoClient
client = MongoClient()
db = client.pymongo_test

collection = db.test_collection

#Documents 

import datetime 
post = {'author': 'Amreeta',
		"text": "How awesome are Ben and Nick?!",
		"tags":["mongodb", "python", "pymongo"],
		"date":datetime.datetime.utcnow()
	
}


#Insert a document

posts = db.posts
post_id = posts.insert_one(post).inserted_id
post_id




print('Our first post id: {0}'.format(post_id))


print('Our first post: {0}'.format(post))



#Excellent resource: https://api.mongodb.com/python/current/tutorial.html