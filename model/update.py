from flask import *
"""藍圖物件可看做一個縮小版的app物件"""
up = Blueprint('up', __name__) # 第一個引數為藍圖名稱，隨便取

@up.route("/update", methods=["PUT"])
def update():
    return "OK"