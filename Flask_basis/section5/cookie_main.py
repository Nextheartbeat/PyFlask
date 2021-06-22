# TODO: Cookie
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/cookie')
def cookie():
    # 通过 request.cookies 读取当前客户端传递的 cookie
    print(request.cookies)
    return request.cookies


@app.route('/cookie/set')
def set_cookie():
    # 创建响应对象
    response = make_response('set cookie')

    # 设置响应头的set_cookie字段, value必须是str/bytes类型
    response.set_cookie('cookie-1', 'value-1', max_age=86400)
    response.set_cookie('cookie-2', 'value-2', max_age=86400)
    # 返回响应对象
    return response


@app.route('/cookie/delete')
def delete_cookie():
    # 创建响应对象
    response = make_response('delete cookies')
    # 通过 response.delete_cookie(cookie名) 删除 cookie
    response.delete_cookie('cookie-1')
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

"""
    特点:
        将数据保存在 客户端 (用户的电脑上), 可以减轻服务器压力
        访问网站时, 浏览器会 自动 将该网站的cookie数据发送给服务器
        使用场景:
            保存一些 不太重要的数据
"""
# TODO: 代码解读

# 定义一个接口，用于读取 cookies 字典数据 request.cookies

# 定义一个接口，用于颁发 cookie 数据
# 1. 实例化 response 对象 通过 make_response 函数
# 2. response.set_cookie(key,value) 设置 cookie
# 3. 返回 response 对象

# 定义一个接口，用于删除 cookie 数据
# 1. 实例化 response 对象 通过 make_response 函数
# 2. response.delete_cookie(key) 删除 cookie
# 3. 返回 response 对象