from home import home


# 使用蓝图定义路由
@home.route('/home')
def index():
    return 'index_home'
