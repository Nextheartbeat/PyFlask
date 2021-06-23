from flask import Blueprint

# 创建蓝图对象
# 可以通过 url_prefix 参数给蓝图定义的路由添加统一的URL资源段前缀
home = Blueprint('home', __name__, url_prefix='/api')

# 导入视图模块
# 也可以使用 from home import views
# 或者 import home.views
# 但是代码的风格不太好，可能会导致循环导入的问题
__import__('home.views')


# 蓝图也可以设置请求钩子 只有访问该蓝图定义的路由时才会触发局部监听
@home.before_request
def before_request():
    print('home before_request')
