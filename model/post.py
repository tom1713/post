from flask import *
import time
from model.db import db
from flask_paginate import Pagination, get_page_parameter

app.secret_key = "123"

"""藍圖物件可看做一個縮小版的app物件"""
ps = Blueprint('ps', __name__) # 第一個引數為藍圖名稱，隨便取

@ps.route("/post", methods=['GET', 'POST'])
def post():
    collection = db.posts
    cur = collection.find()
    if request.method == 'GET':
        per_page = int(request.args.get('per_page', 10))  # 每一頁顯示數量
        page = request.args.get(get_page_parameter(), type=int, default=1) # 獲取當前為第幾頁
        url_count = collection.count_documents({})
        pagination = Pagination(page=page, total=url_count, per_page=per_page, css_framework='bootstrap')
        return render_template('post.html', page=page, per_page=per_page, count=str(url_count), pagination=pagination, says=cur)
        # return render_template('post.html', says=users)
    if request.method == 'POST':
        if "nickname" not in session:
            return render_template('signin.html')
        title = request.form.get('say_title')
        text = request.form.get('say')
        user = request.form.get('say_user')
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        result = collection.insert_one({
            "title" : title,
            "text" : text,
            "user" : session["nickname"],
            "date" : date,
            "email" : session["email"],
        })
        return redirect(url_for('ps.post'))
    return render_template("/")