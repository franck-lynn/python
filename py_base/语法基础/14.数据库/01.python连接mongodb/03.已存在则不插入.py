import pymongo

# 连接数据量
client = pymongo.MongoClient("mongodb://localhost:27017")
# 使用数据量
db = client['test']

# 进入集合
coll = db['actors']

# 数据
# 有这个字段就不插入, 
# 没有这个集合也不更新, 就插入
# 如果是 False, 则没有找到这个集合时,不插入
x = coll.update_one(
    {"name": "aaa"},
    {
        "$set": {"blog": "abc1234"}
    },
    True
)
print(x)

# 有就更新一个新的字段 {"key": 123}
# "$setOnInsert" 是集合没有的时候才插入, 
#                有这个集合则不插入
y = coll.update_one(
    {"name": "aaa"},
    {
        "$set": {"key1": 123}
    }, 
    # 默认就是 true, true, false 作用只是控制有没有这个集合时的行为
    False
)
print(y)