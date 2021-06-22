# TODO: 异常处理
from flask import Flask, abort

app = Flask(__name__)


# 被装饰的函数需要接受一个参数, 用于接受错误对象
# 捕获http错误
@app.errorhandler(404)
def error_404(error):  # 一旦进行捕获, 要求必须定义形参接收具体错误信息
    return f"<h3>您访问的页面去浪迹天涯了</h3>\n {error}"


# 还可以捕获系统内置错误
@app.errorhandler(ZeroDivisionError)
def error_zero(error):
    return f"除数不能为0 \n {error}"


@app.route('/')
def http_404():
    # 通过 about 抛出特定的 http 异常
    abort(404)  # 主动抛出异常 (只能抛出http错误)
    return "index"


@app.route('/zero')
def zero():
    a = 1 / 0
    return 'zero'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)


"""
    flask对 HTTP错误 进行了封装, 可以捕获http错误, 也可以主动抛出http错误
"""
# TODO
# 定义 http 错误处理
# @app.errorhandler(http错误状态码 400~600)
# def 函数(error) error 表示错误信息对象
#     返回响应
#
# 定义特定异常类错误处理
# @app.errorhandler(异常类)
# def 函数(error) error 表示异常类对象
#     返回响应

# 定义两个接口，一个接口抛出 http 错误，一个抛出特定异常类对象
#    abort(http错误状态码) 可以抛出 http 错误
