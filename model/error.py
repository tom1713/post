from flask import *
"""藍圖物件可看做一個縮小版的app物件"""
er = Blueprint('er', __name__) # 第一個引數為藍圖名稱，隨便取

# /error?msg=錯誤訊息
@er.route("/error")
def error():
    message = request.args.get("msg", "發生錯誤，請聯繫客服")
    return render_template("error.html", message = message)