import time, json
#初始化資料庫連線
import pymongo
client = pymongo.MongoClient("mongodb+srv://user:user123@cluster0.hpcbu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.member_system
print("資料庫連線建立成功")