import time, json
#初始化資料庫連線
import pymongo
client = pymongo.MongoClient("mongodb://root:root123@cluster0.hpcbu.mongodb.net/?retryWrites=true&w=majority")
# client = pymongo.MongoClient("mongodb://root:root123@cluster0.hpcbu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tls=True)
db = client.member_system
print("資料庫連線建立成功")