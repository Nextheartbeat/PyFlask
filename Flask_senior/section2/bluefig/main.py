from flask import Flask

from home import home

app = Flask(__name__)

# 注册蓝图对象
app.register_blueprint(home)


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='127.0.0.1', port=8000, debug=True)

