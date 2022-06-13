from flask import *
from model.db import db

"""藍圖物件可看做一個縮小版的app物件"""
sin = Blueprint('sin', __name__) # 第一個引數為藍圖名稱，隨便取

@sin.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        #從前端取得使用者的輸入
        email = request.form["email"]
        password = request.form["password"]
        #和資料庫互動
        collection = db.users
        #檢查信箱密碼是否正確
        result = collection.find_one({
            "$and":[
                {"email" : email},
                {"password" : password}
            ]
        })
        #找不到對應的資料，登入失敗，導向到錯誤頁面
        if result == None:
            return redirect("/error?msg=帳號或密碼輸入錯誤")
        #登入成功，導向到會員頁面
        session["nickname"] = result["nickname"]
        return redirect("/member")
    return render_template("/signin.html")