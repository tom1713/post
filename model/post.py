from flask import *
import time
from model.db import db

"""藍圖物件可看做一個縮小版的app物件"""
ps = Blueprint('ps', __name__) # 第一個引數為藍圖名稱，隨便取

@ps.route("/post", methods=['GET', 'POST'])
def post():
    collection = db.posts
    cur = collection.find()
    users = cur
    if request.method == 'GET':
            return render_template('post.html', says=users)
    if request.method == 'POST':
        title = request.form.get('say_title')
        text = request.form.get('say')
        user = request.form.get('say_user')
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        result = collection.insert_one({
            "title" : title,
            "text" : text,
            "user" : user,
            "date" : date
        })
        print(result)
        return redirect(url_for('post'))
    return render_template("/index")