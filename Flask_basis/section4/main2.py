# TODO: 响应 -设置响应数据
from flask import Flask, make_response

app = Flask(__name__)


# Flask中 视图函数的返回值可以设置三个, 分别对应 响应体, 响应状态码, 响应头字典 && 也可以是返回 响应体, 响应状态码 或者 响应体, 响应头字典
@app.route('/response_tuple')
def response_tuple():
    # 返回值: 响应体, 响应状态码, 响应头字典
    return 'demo1', 200, {'A': 40}


# 可以通过 make_response 函数创建响应对象(Response对象)来 自定义响应头 等信息，并且返回该响应对象。
@app.route('/response_obj')
def response_obj():
    response = make_response('response content')
    response.headers['my-header'] = 'my-value'
    return response


# 如果接口需要返回 JSON 数据, 可以直接返回一个字典
@app.route('/response_json')
def response_json():
    data = {
        "name": "NextHeartbeat",
        "age": 18
    }
    return data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

"""
Flask中设置响应数据主要有两种方式:
    设置多个返回值
    自定义响应对象
"""
