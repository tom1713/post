from flask import *
"""藍圖物件可看做一個縮小版的app物件"""

import time, json
#初始化資料庫連線
import pymongo
client = pymongo.MongoClient("mongodb+srv://root:root123@cluster0.hpcbu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.member_system
print("資料庫連線建立成功")

#初始化 flask 伺服器
from flask import *
from model.member import mb
from model.register import regs
from model.signin import sin
from model.error import er
from model.signout import so
from model.post import ps
from model.db import db

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

#處理路由
@app.route("/index")
def index():
    return render_template("index.html")

#啟動伺服器
app.run(port=3000, debug=True)