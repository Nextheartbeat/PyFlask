# 导入Flask类
from flask import Flask

# 创建Flask应用
app = Flask(__name__)

# 绑定路由
@app.route('/')
def index():
    return 'hello FLask'


# 启动web服务
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000)
"""
    app.run() 可以接受额外的参数
        host: 绑定的ip(域名) 0.0.0.0
        port: 监听的端口号
        debug: 是否开启调试模式。开启后可以在网页上显示python错误，更新代码后测试服务器自动重启。 app.run(host='0.0.0.0', port=8000, debug=True)
        
    通过命令行启动web服务
        export FLASK_APP=xx.py  # 指定flask应用所在的文件路径
        export FLASK_ENV=development  # 设置项目的环境, 默认是生产环境
        flask run -h 0.0.0.0 -p 8000  # 启动测试服务器并接受请求
"""