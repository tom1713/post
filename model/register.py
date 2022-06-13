from flask import *
from model.db import db

"""藍圖物件可看做一個縮小版的app物件"""
regs = Blueprint('regs', __name__) # 第一個引數為藍圖名稱，隨便取

@regs.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #從前端接收資料
        nickname = request.form["nickname"]
        email = request.form["email"]
        password = request.form["password"]
        print(nickname, email, password)
        #根據收到的資料，跟資料庫互動
        collection = db.users
        #檢查會員集合中是否有相同 email 的文件資料
        result = collection.find_one({
            "email" : email
        })
        if result != None :
            return redirect("/error?msg=信箱已經被註冊")
        #把資料放進資料庫，完成註冊
        collection.insert_one({
            "nickname" : nickname,
            "email" : email,
            "password" : password
        })
        return render_template("register.html")
    return render_template("register.html")
