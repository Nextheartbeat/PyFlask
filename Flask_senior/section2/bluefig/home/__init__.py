from flask import Blueprint

# 创建蓝图对象
home = Blueprint('home', __name__)

# 导入视图模块
# 也可以使用 from home import views
# 或者 import home.views
# 但是代码的风格不太好，可能会导致循环导入的问题
__import__('home.views')
