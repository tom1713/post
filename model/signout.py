from flask import *
"""藍圖物件可看做一個縮小版的app物件"""
so = Blueprint('so', __name__) # 第一個引數為藍圖名稱，隨便取

@so.route("/signout")
def signout():
    #移除session中的會員資訊
    del session["nickname"]
    return redirect("/index")
