# TODO: 定义路由
from flask import Flask

app = Flask(__name__)


# 只接受 post,get 请求
@app.route('/index', methods=['post', 'get'])
def index():
    return 'index'


if __name__ == '__main__':
    # 打印路由信息, rule 是 werkzeug.routing.Rule 类对象
    for rule in app.url_map.iter_rules():
        print(f'{rule} {rule.methods} {rule.endpoint}')
    app.run(host='0.0.0.0', port=8000, debug=True)

"""
    定义路由的三个细节
        路由对应的URL必须以 / 开头
        app.route() 的 methods 参数 指定路由支持的请求方式，如果客户端发起的请求方式不在 methods 范围内会返回 405
        app.url_map 获取应用所有路由规则
        路由规则中主要包含 (URL资源段、支持的请求方式、视图函数标记) 三部分内容
        (/index 
            {'OPTIONS', 'GET', 'HEAD', 'POST'} index
                /static/<path:filename> {'OPTIONS', 'GET', 'HEAD'} static)
"""