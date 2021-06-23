from flask import Blueprint

# 创建蓝图对象
user = Blueprint('user', __name__)


# 导入视图模块
# 也可以使用 from user import user
# 或者 import user.views
# 但是代码的风格不太好，可能会导致循环导入的问题
__import__('user.views')