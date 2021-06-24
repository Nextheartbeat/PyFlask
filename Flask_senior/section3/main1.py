# TODO: 上下文
from flask import Flask, g, current_app

app = Flask(__name__)


@app.route('/index')
def index():
    # 打印
    print(current_app)
    print(current_app.url_map)
    return 'index'


if __name__ == '__main__':
    # print(current_app)  # 只能在请求范围内使用, 这里会报错
    # print(g)
    app.run(host='127.0.0.1', port=8000, debug=True)

"""
current_app
    会自动引用创建的Flask对象, 需要在项目的其他文件中使用app时, 应该通过current_app来获取, 可以减少循环导入问题
    只能在请求过程执行代码中使用(也就是从请求钩子-->视图函数-->请求钩子)
    如果在请求过程之外调用会报错
"""