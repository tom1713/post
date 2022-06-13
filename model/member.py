from flask import *
"""藍圖物件可看做一個縮小版的app物件"""
mb = Blueprint('mb', __name__) # 第一個引數為藍圖名稱，隨便取

@mb.route('/member')
def member():
    if "nickname" in session:
        return render_template("member.html")
    else:
        return redirect("/")
