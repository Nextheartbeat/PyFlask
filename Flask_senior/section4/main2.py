# TODO: 访问限制
import functools
from flask import Flask, session, g, abort

app = Flask(__name__)

app.secret_key = 'Nextheartbeat'


def login_required(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if g.is_login:
            return f(*args, **kwargs)
        else:
            abort(401)

    return wrapper


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


@app.before_request
def set_is_login():
    # 使用g 变量来传递数据
    if 'username' in session:
        g.is_login = True
    else:
        g.is_login = False


@app.route('/userinfo')
def user_info():
    # 判断用户是否已经登录
    if g.is_login:
        return 'userinfo'
    abort(401)


# TODO: 限制访问, 只有登录过的用户才可以访问接口, 以装饰器装饰, 如果g.is_login==True ,就调用装饰器, 否则 about401
@app.route('/update_password')
@login_required
def update_password():
    return 'update_password'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

"""
    import functools
    系统内置的装饰器, 主要用于装饰器中的闭包函数
    作用是将被装饰的函数(wrapper)的函数信息替换为指定函数(f)的函数信息 (包括 __name__ 函数名, __doc__ 函数注释等)
"""