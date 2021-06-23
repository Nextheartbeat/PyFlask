from user import user


# 使用蓝图对象来定义路由
@user.route('/user')
def index():
    return 'index_user'
