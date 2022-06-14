import time, json
#初始化資料庫連線
import pymongo
client = pymongo.MongoClient("mongodb://root:root123@cluster0.hpcbu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority0&autoReconnect=true&socketTimeoutMS=360000&connectTimeoutMS=360000")
db = client.member_system
print("資料庫連線建立成功")