# TODO: 路由变量
from flask import Flask

app = Flask(__name__)


# 定义路由变量
@app.route('/user/<user_id>')
def index(user_id):
    return f"user_id: {user_id}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)


"""
    route: http://127.0.0.1:8000/user/12
    print user_id: 12
"""