# TODO: 响应 -访问静态资源
from flask import Flask

app = Flask(__name__,
            static_folder="static",  # 设置静态文件存储路径
            static_url_path='/static',  # 设置静态文件的URL访问路径 如 127.0.0.1:5000/static/test.png
            )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

"""
    将静态资源放入到 项目的 static 文件夹中
        通过内置的静态资源的访问路由, URL路径格式为 /static/<filename>
        如 static目录放入文件 test.png, 则访问URL为 http://127.0.0.1:5000/static/test.png
"""