# TODO: 调用 config 配置文件
from flask import Flask, session
from config import Production, Development

app = Flask(__name__)

# 加载配置
app.config.from_object(Development)


@app.route('/index')
def index():
    # 设置 session 用于测试配置是否生效
    session['name'] = 'NextHeartbeat'
    # 读取配置
    print(app.config.get('PERMANENT_SESSION_LIFETIME'))
    print(app.config.get('ENV'))
    return 'index_config'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)


