import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['test']

dblist = myclient.list_database_names()

# 判断数据库是否已经存在
if 'test' in dblist:
    print("数据库已存在")

collist = mydb.list_collection_names()
if 'actors' in collist:
    print("集合已存在")



    
    