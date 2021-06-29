# TODO: app.config 加载配置
from datetime import timedelta

from flask import Flask, session

app = Flask(__name__)

# config 属性用于设置配置, 要注意这里的配置项都是大写
app.config['SECRET_KEY'] = 'test'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route('/index')
def index():
    # 设置 session 用于测试配置是否生效
    session['name'] = 'NextHeartbeat'
    # 读取配置
    print(app.config.get('PERMANENT_SESSION_LIFETIME'))
    return 'index'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
