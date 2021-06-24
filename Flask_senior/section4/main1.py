# TODO: 综合认证 -统一认证
from flask import Flask, session, g, abort

app = Flask(__name__)

# 开启 app 的 session
app.secret_key = 'Nextheartbeat'


# 模拟用户登录
@app.route('/login')
def login():
    """登录"""
    session['username'] = 'Next'
    return '登录'


@app.route('/logout')
def logout():
    """退出"""
    if 'username' in session:
        del session['username']
    return '退出成功'


# 需求1: 所有视图都需要获取用户是否已经登录
# 解决办法: 用钩子函数进行封装减少代码冗余
# 使用g变量来传递数据
@app.before_request
def set_is_login():
    # 使用g 变量来传递数据
    if 'username' in session:
        g.is_login = True
    else:
        g.is_login = False


# 定义视图获取用户信息
# 视图中判断 g.is_log

@app.route('/userinfo')
def user_info():
    # 判断用户是否已经登录
    if g.is_login:
        return 'userinfo'
    abort(401)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

"""
需求: 获取用户身份
分析: 除了静态资源, 基本所有视图都需要获取用户身份, 每个视图单独获取出现大量的代码冗余
解决办法: 设置 请求钩子, 并通过 g变量 将数据传递给视图函数
"""

# TODO:
# 开启 app 的 session
# app.secret_key = 秘钥

# 定义一个登录接口，模拟用户登录
# 用户登录成功时，往session中设置一个username字段

# 定义一个退出登录接口，模拟用户退出
# 将 session 中的 username 字段删除

# 定义一个请求钩子 通过 @app.before_request
# 逻辑: 如果 session 中包含 username 字段就说明用户已经登录，设置 g.is_login = True,否则 g.is_login = False

# 定义一个接口，模拟获取用户信息
# 逻辑: 如果 g.is_login==True 就返回用户信息，否则 abort(401)
