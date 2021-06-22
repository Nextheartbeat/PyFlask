# TODO: Session
from datetime import timedelta

from flask import Flask, session

app = Flask(__name__)

# 设置应用秘钥会被用于session签名
app.secret_key = 'NextHeartbeat'
# 设置session过期时间 默认31天
print(f'默认过期时间{app.permanent_session_lifetime}')
# 通过赋值一个 timedelta 对象来修改 session 的过期时间
app.permanent_session_lifetime = timedelta(days=7)


@app.route('/session')
def get_session():
    # session是一个类字典对象
    print(session)
    return {key: value for key, value in session.items()}


@app.route('/session/set')
def set_session():
    # session 是一个类字典对象, 对其取值/赋值 就可以实现session数据的读写

    # 记录session数据
    session['username'] = 'jiweiwang'
    session['age'] = 18

    return "set session"


@app.route('/session/delete')
def delete_session():
    # 使用 del 来删除 session 的 key, 但是要判断 key 是否在 session, 如果不判断可能会出现异常
    if 'username' in session:
        del session['username']

    return "delete session"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

# TODO: 注意 flask 的默认 session 机制 没有将 session 数据保存到服务器的数据库中, 而是将 session 数据编码后保存到了 cookie 中 (签名 cookie 机制)
"""
    特点:
        将数据保存在 服务端 (服务器的数据库中), 安全性更高
        使用场景:
            保存一些 重要/敏感的数据
"""
