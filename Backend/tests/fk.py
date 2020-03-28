import pymongo

client = pymongo.MongoClient("mongodb+srv://root:root@cluster0-cg3ab.mongodb.net/test?retryWrites=true&w=majority")


doc_db = client["documents"]['images']

doc_db.drop()