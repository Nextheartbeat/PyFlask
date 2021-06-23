from flask import Flask


app = Flask(__name__)
from user import user
from home import home

# 注册蓝图对象
app.register_blueprint(home)
app.register_blueprint(user)


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='127.0.0.1', port=8000, debug=True)