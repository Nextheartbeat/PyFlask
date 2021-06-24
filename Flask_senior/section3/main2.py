# TODO: 上下文 g容器
from flask import Flask, g, current_app

app = Flask(__name__)


@app.before_request
def set_g():
    # 设置 name 属性
    g.name = 'Nextheartbeat'
    print('before_request')


@app.route('/g')
def read_g():
    print(g.name)
    return 'read g'


if __name__ == '__main__':
    # print(g)  # 只能在请求范围内使用, 这里会报错
    app.run(host='127.0.0.1', port=8000, debug=True)

"""
g 数据容器:
    flask 给开发者预留的一个容器, 用于记录自定义数据
    g 使用场景在请求处理过程过程共享数据
"""