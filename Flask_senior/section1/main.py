# TODO: 请求钩子
from flask import Flask

app = Flask(__name__)


# 每次执行视图函数之前调用, 对请求进行一些准备处理, 如参数解析, 黑名单过滤, 数据统计
@app.before_request
def before_request_1():
    print('before_request 1')


@app.before_request
def before_request_1():
    print('before_request 2')


# 每次执行视图函数之后(已经包装为响应对象)调用, 对响应进行一些加工处理, 如设置统一响应头, 设置数据的外包装
@app.after_request
def after_request_1(response):  # 必须定义形参接收响应对象
    print('after_request_1')
    return response


@app.after_request
def after_request_2(response):  # 必须定义形参接收响应对象
    print('after_request_2')
    return response


# web应用被第一次请求前调用, 可以进行web应用初始化处理, 如数据库连接
@app.before_first_request
def before_first_request():
    print('before_first_request')

# 每次执行视图函数之后调用, 无论是否出现异常都会执行, 一般用于请求收尾, 如资源回收, 异常统计
@app.teardown_request
def teardown_request(error):  # 必须定义形参来接收具体错误信息, 如果没有错误, error=None
    print('teardown_request: %s' % error)


@app.route('/hook')
def hook():
    print('执行视图!')
    return 'index'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

"""
# TODO:
# @app.before_request 装饰请求预处理的钩子
# def xxx(): 返回 None

# @app.after_request 装饰响应预处理的钩子
# def xxx(response):  response 参数是视图函数或者前一个钩子的返回值
#     需要返回一个 response

# @app.before_first_request 装饰第一个请求处理之前执行的钩子
# 这个钩子只会被运行一次，一般用于web应用初始化处理

# @app.teardown_request 装饰每个视图调用之后的钩子
# def xxx(error): 如果视图函数执行失败了，这里的 error 是错误信息，否则 error 是 None
"""

"""
# 执行结果: 
    before_first_request
    before_request 1
    before_request 2
    执行视图!
    after_request_2
    after_request_1
    teardown_request: None
"""