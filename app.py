#初始化 flask 伺服器
from flask import *
import os
from model.member import mb
from model.register import regs
from model.signin import sin
from model.error import er
from model.signout import so
from model.post import ps
from model.db import db
from model.update import up
from flask_paginate import Pagination, get_page_parameter

app = Flask(
    __name__,
    static_folder = "static", 
    static_url_path = "/"
)

app.secret_key = "123"

app.register_blueprint(mb)
app.register_blueprint(regs)
app.register_blueprint(sin)
app.register_blueprint(ps)
app.register_blueprint(er)
app.register_blueprint(so)
app.register_blueprint(up)

#處理路由
@app.route("/", methods = ["GET", "POST"])
def index():
    collection = db.posts
    cur = collection.find()
    per_page = int(request.args.get('per_page', 10))  # 每一頁顯示數量
    page = request.args.get(get_page_parameter(), type=int, default=1) # 獲取當前為第幾頁
    url_count = collection.count_documents({})
    pagination = Pagination(page=page, total=url_count, per_page=per_page, css_framework='bootstrap')
    return render_template('index.html', page=page, per_page=per_page, count=str(url_count), pagination=pagination, says=cur)

# app.run(debug=True)

#啟動伺服器
port = int(os.environ.get('PORT', 0))
app.run(host='0.0.0.0', port=port, debug=True)