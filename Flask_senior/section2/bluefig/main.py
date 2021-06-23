from flask import Flask

from home import home

app = Flask(__name__)

# 注册蓝图对象
app.register_blueprint(home)

if __name__ == '__main__':
    print(app.url_map)
    app.run(host='127.0.0.1', port=8000, debug=True)

"""
蓝图的作用: 实现Flask项目 模块化
项目模块化主要是 将业务以功能模块进行划分, 每个功能模块对应一个包, 用于存放和其有关的视图/工具/模型文件等, 如home, user
对于大型项目, 一般 每个功能模块对应创建一个蓝图, 由多个蓝图代替应用来分别管理各模块的视图
"""

"""
--------- project # 工程目录
  |------ main.py # 启动文件
  |------ user  # 用户模块
  |  |--- __init__.py  # 包的初始化文件, 此处创建管理用户模块的蓝图对象
  |  |--- views.py  # 视图文件
  |  |--- ...
  |
  |------ home # 首页模块
  |  |--- __init__.py  # 包的初始化文件, 此处创建管理首页模块的蓝图对象
  |  |--- views.py  # 视图文件
  |  |--- ...
  |...
"""
