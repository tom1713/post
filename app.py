#初始化 flask 伺服器
from flask import *
# from model.member import mb
# from model.register import regs
# from model.signin import sin
# from model.error import er
# from model.signout import so
# from model.post import ps
# from model.db import db

app = Flask(
    __name__,
    static_folder = "static", 
    static_url_path = "/"
)

app.secret_key = "123"

# app.register_blueprint(mb)
# app.register_blueprint(regs)
# app.register_blueprint(sin)
# app.register_blueprint(ps)
# app.register_blueprint(er)
# app.register_blueprint(so)

#處理路由
@app.route("/")
def index():
    return "OK"
    #render_template("index.html")

#啟動伺服器
app.run()