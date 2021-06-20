# TODO: 路由转换器
from flask import Flask

app = Flask(__name__)


# 定义路由变量
@app.route('/user/<user_id>')
def index(user_id):
    return f"user_id: {user_id}"


# string
@app.route('/string/<string(minlength=6,maxlength=16):username>')
def username(username):
    return f"username: {username}"


# int
@app.route('/int/<int(min=10,max=100):age>')
def age(age):
    return f"age: {age}"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)


"""
    route: http://127.0.0.1:8000/user/12
    print user_id: 12
    
    route: http://127.0.0.1:8000/string/aaaaaaaaaaaaaa
    print username: aaaaaaaaaaaaaa 
    (最小长度为: 6, 最大长度为16, 否则: Not Found)
    
    route: http://127.0.0.1:8000/int/10
    print age: 10
    (最小值为: 10, 最大值为:100, 否则: Not Found)
"""


"""
    路由转换器的作用是 对URL传递的参数进行格式校验, 类似Django设置URL时的正则表达式参数
    格式: /xx/<转换器名(可选的参数):路由变量>
    内置路由转换器:
        string: 默认的转换器，只是提取出参数，参数数据格式是字符串。werkzeug.routing.UnicodeConverter
        参数:
        minlength: 字符串最小长度
        maxlength: 字符串最大长度
        length: 字符串长度，和上面两个参数不一起使用
        例如: <name>
        例如: <string:name>
        例如: <string(minlength=8,maxlength=16):username>
        
        int: 将参数转化为整数。 werkzeug.routing.IntegerConverter
        参数: min: 最小值(包含)
        max: 最大值(包含)
        fixed_digits: 最多数字字符的个数
        signed: 是否是带符号的整数字符串
        例如: <int:age>
        例如: <int(min=0,max=100):age>
        
        float: 将参数转化为浮点数。werkzeug.routing.FloatConverter
        参数:
        min: 最小值(包含)
        max: 最大值(包含)
        例如: <float:length>
        例如: <float(min=0,max=100):age>
"""
