from flask import *
import time
from model.db import db
from bson.objectid import ObjectId
"""藍圖物件可看做一個縮小版的app物件"""
up = Blueprint('up', __name__) # 第一個引數為藍圖名稱，隨便取

@up.route("/updated", methods=["POST"])
def updated():
    if request.method == "POST":
        title = request.form['say_title']
        text = request.form['say']
        _id = request.form['_id']
        collection = db.posts
        result1 = collection.update_one({
            "_id" : ObjectId(_id)
        }, {"$set":
        {"title" : title},
        })
        result2 = collection.update_one({
            "_id" : ObjectId(_id)
        }, {"$set":
        {"text" : text
        }})
        result3 = collection.update_one({
            "_id" : ObjectId(_id)
        }, {"$set":
        {"date" : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        }})
        print("符合條件的文件數量:", result1.matched_count)
        print("實際更新的文件數量:", result1.modified_count)
        print("符合條件的文件數量:", result2.matched_count)
        print("實際更新的文件數量:", result2.modified_count)
        print("符合條件的文件數量:", result3.matched_count)
        print("實際更新的文件數量:", result3.modified_count)
    return redirect(url_for('ps.post'))