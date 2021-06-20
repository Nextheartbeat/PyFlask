# TODO: 自定义转换器
from flask import Flask

from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 定义转换器类, 继承BaseConverter
class MyBoolConverter(BaseConverter):
    # 用于对路径参数进行匹配
    regex = r"False|True"

    # 对路径原始参数进行转换, 它的返回值就是路由函数参数接受的值
    def to_python(self, value):
        if value == "True":
            return True
        else:
            return False


app.url_map.converters['bool'] = MyBoolConverter


@app.route('/my_converter/<bool:is_vip>')
def is_vips(is_vip):
    return f"is_vip : {is_vip}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

"""
    route: http://127.0.0.1:8000/my_converter/True
    print is_vip : True
    
    route: http://127.0.0.1:8000/my_converter/True
    print is_vip : False
    
"""


"""
    除了使用内置的变量转换器, 开发者还可以自定义转换器, 更加灵活的校验路由变量
        使用自定义转换器的步骤:
        1. 定义转换器类, 继承 werkzeug.routing.BaseConverter
            1. 设置 regex 属性 (正则匹配规则)，用于对路径参数进行匹配，如果请求的路径没有匹配上就返回 404
            2. 定义 to_python 方法对路径原始参数进行转换，它的返回值就是路由函数参数接受的值
           这个方法接收一个参数，这个参数就是路径中提取的字符串
        2. 应用添加自定义转换器 `app.url_map.converters[转换器名]=转换器类`
        3. 使用自定义路由转换器 @app.route('/some_path/<转换器名:is_vip>')
"""
