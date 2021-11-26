import pymongo

# 连接数据量
client = pymongo.MongoClient("mongodb://localhost:27017")
# 使用数据量
db = client['test']
# 进入集合
coll = db['actors']

# 数据
dict = {"name": "aaa", "alexa": "10000", "url": "https://www.runoob.com"}
# 插入数据
x = coll.insert_one(dict)
print(x.inserted_id)

